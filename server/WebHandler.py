import json
import os
from importlib import reload

from aiohttp import web

import server.FileService as FileService
from utils.Configs import config
from utils.JsonUtils import add_conv, is_datetime, datetime_encode, json_serialize_helper
from utils.ObjectUtils import not_none_f


async def _body(request: web.Request) -> str:
    payload = ''
    stream = request.content
    while not stream.at_eof():
        line = await stream.read()
        payload += line.decode()
    return payload


def _success_response(aa):
    # return web.json_response({"status": "success", **aa})
    return web.Response(body=json.dumps({"status": "success", **aa}, default=json_serialize_helper))


def _failure_json(aa: dict or object):
    # return web.json_response({"status": "success", **aa})
    if isinstance(aa, dict):
        return json.dumps({"status": "error", **aa}, default=json_serialize_helper)
    else:
        return json.dumps({"status": "error", 'message': str(aa)})


async def _payload_json(request: web.Request, quiet: bool = False) -> dict or None:
    try:
        payload = (await (_body(request)) or '').strip()
        return payload and json.loads(payload) or {}
    except json.JSONDecodeError as err:
        if quiet:
            return None
        else:
            raise web.HTTPBadRequest(text=f"cannot parse json: {str(err)}")


class WebHandler:
    """aiohttp handler with coroutines."""

    def __init__(self) -> None:
        os.chdir(config.dir)
        reload(FileService)

    async def handle(self, request: web.Request, *args, **kwargs) -> web.Response:
        """Basic coroutine for connection testing.

        Args:
            request (Request): aiohttp request.

        Returns:
            Response: JSON response with status.
        """

        return web.json_response(data={
            'status': 'success'
        })

    async def change_dir(self, request: web.Request, *args, **kwargs) -> web.Response:
        """Coroutine for changing working directory with files.

        Args:
            request (Request): aiohttp request, contains JSON in body. JSON format:
            {
                "path": "string. Directory path. Required",
            }.

        Returns:
            Response: JSON response with success status and success message or error status and error message.

        Raises:
            HTTPBadRequest: 400 HTTP error, if error.
        """
        if request.method == 'GET':
            return _success_response({"result": FileService.get_current_dir()})

        data = await _payload_json(request)
        path = not_none_f(lambda: request.match_info.get('urlpath'), lambda: data.get('path'))
        try:
            FileService.change_dir(path, bool(not_none_f(lambda: data.get('autocreate'), lambda: config.autocreate)))
            return _success_response({"message": "OK"})
        except (RuntimeError, ValueError) as err:
            raise web.HTTPBadRequest(text=_failure_json(err))

    async def get_files(self, request: web.Request, *args, **kwargs) -> web.Response:
        """Coroutine for getting info about all files in working directory.

        Args:
            request (Request): aiohttp request.

        Returns:
            Response: JSON response with success status and data or error status and error message.
        """
        filename = request.match_info.get('urlpath')
        return _success_response({"data": (FileService.get_files(filename))})

    async def get_file_data(self, request: web.Request, *args, **kwargs) -> web.Response:
        """Coroutine for getting full info about file in working directory.

        Args:
            request (Request): aiohttp request, contains filename and is_signed parameters.

        Returns:
            Response: JSON response with success status and data or error status and error message.

        Raises:
            HTTPBadRequest: 400 HTTP error, if error.
        """

        filename = request.match_info.get('filename')
        if filename is None:
            raise web.HTTPBadRequest(text=_failure_json("No filename specified"))
            # raise web.HTTPBadRequest(text="No filename specified")
        try:
            return _success_response({"data": (FileService.get_file_data(filename))})
        except (RuntimeError, ValueError) as err:
            raise web.HTTPBadRequest(text=_failure_json(err))

    async def create_file(self, request: web.Request, *args, **kwargs) -> web.Response:
        """Coroutine for creating file.

        Args:
            request (Request): aiohttp request, contains JSON in body. JSON format:
            {
                'filename': 'string. filename',
                'content': 'string. Content string. Optional',
            }.

        Returns:
            Response: JSON response with success status and data or error status and error message.

        Raises:
            HTTPBadRequest: 400 HTTP error, if error.
        """

        try:
            urlpath = request.match_info.get('urlpath')
            data = await _payload_json(request) if urlpath is None \
                else {'filename': urlpath, "content": await _body(request)}
            return _success_response({"data": (FileService.create_file(data['filename'], data.get("content"), True))})
        except (RuntimeError, ValueError) as err:
            raise web.HTTPBadRequest(text=_failure_json(err))

    async def delete_file(self, request: web.Request, *args, **kwargs) -> web.Response:
        """Coroutine for deleting file.

        Args:
            request (Request): aiohttp request, contains filename.

        Returns:
            Response: JSON response with success status and success message or error status and error message.

        Raises:
            HTTPBadRequest: 400 HTTP error, if error.

        """

        if (filename := request.match_info.get('filename')) is None:
            raise web.HTTPBadRequest(text="No filename specified")
        try:
            FileService.delete_file(filename)
            return _success_response({"message": "File is deleted"})
        except (RuntimeError, ValueError) as err:
            raise web.HTTPBadRequest(text=_failure_json(err))
