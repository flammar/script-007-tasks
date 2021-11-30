import json
import os
import datetime
from importlib import reload

from aiohttp import web

import server.FileService as FileService
from utils.Configs import config
from utils.JsonUtils import add_conv
from utils.ObjectUtils import not_none, not_none_f


def is_datetime(obj):
    return isinstance(obj, datetime.datetime)


def is_datetime_ser(obj):
    return isinstance(obj, dict) and obj.get("__type__") == "datetime.datetime" and "isoformat" in obj


def datetime_encode(obj: datetime.datetime):
    return {"__type__": "datetime.datetime", "isoformat": obj.isoformat()}


def datetime_decode(obj: dict):
    return datetime.datetime.fromisoformat(obj["isoformat"])


async def get_body(request: web.Request) -> str:
    payload = ''
    stream = request.content
    while not stream.at_eof():
        line = await stream.read()
        payload += line.decode()
    return payload


def _success_response(aa):
    # return web.json_response({"status": "success", **aa})
    return web.Response(body=json.dumps({"status": "success", **aa}, default=add_conv(is_datetime, datetime_encode)))


class WebHandler:
    """aiohttp handler with coroutines."""

    def __init__(self) -> None:
        # TODO: fix this
        # if bool(config.dir):
        os.chdir(config.dir)
        reload(FileService)
        # FileService.change_dir(dir_from_config)

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

        payload = (await get_body(request) or '').strip()
        data = payload and json.loads(payload) or {}
        path = not_none_f(lambda: request.match_info.get('urlpath'), lambda: data.get('path'))
        FileService.change_dir(path, bool(not_none_f(lambda: data.get('autocreate'), lambda: config.autocreate)))
        return _success_response({"message": "OK"})

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

        # TODO: implement this
        filename = not_none_f(lambda: request.match_info.get('filename'))
        return _success_response({"data": (FileService.get_file_data(filename))})

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

        # TODO: implement this
        payload = (await get_body(request) or '').strip()
        data = payload and json.loads(payload) or {}
        filename = data['filename']
        content = data.get("content")
        res = FileService.create_file(filename, content, True)
        return _success_response({"data": res})

    async def delete_file(self, request: web.Request, *args, **kwargs) -> web.Response:
        """Coroutine for deleting file.

        Args:
            request (Request): aiohttp request, contains filename.

        Returns:
            Response: JSON response with success status and success message or error status and error message.

        Raises:
            HTTPBadRequest: 400 HTTP error, if error.

        """

        # TODO: implement this
        payload = (await get_body(request) or '').strip()
        data = payload and json.loads(payload) or {}
        filename = data['filename']
        FileService.delete_file(filename)
        return _success_response({"message": "File is deleted"})
