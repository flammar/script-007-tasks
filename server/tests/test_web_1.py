import os
from http import HTTPStatus
from server.tests.TestUtils import _random_filename, _random_text, in_random_dir

import server

import pytest

from server import FileService
from server.tests.TestUtils import _random_filename, _random_text
import utils.WebHandlerUtils
import utils.JsonUtils


@pytest.fixture(scope='function')
def web_server():
    app = utils.WebHandlerUtils.get_aiohttp_server()
    yield app


# @pytest.mark.parametrize("filename, content, exists", [
#     ('README1.txt', b'123', False),
#     ('README1.txt', b'12', True),  # shorter size, same file
#     ('README3.txt', b'1\\2/3:4{}5\n6\r7', False),  # use different symbols
# ])
@pytest.mark.parametrize("filename, content", [
    ('README1.txt', b'123'),
    ('README1.txt', b'12'),  # shorter size, same file
    ('README3.txt', b'1\\2/3:4{}5\n6\r7'),  # use different symbols
])
# async def test_create_file(filename, content, exists, web_server, aiohttp_client, aiohttp_unused_port, tmp_dir):
async def test_create_file(filename, content, web_server, aiohttp_client, aiohttp_unused_port):
    app = web_server
    client = await aiohttp_client(app, server_kwargs={'port': aiohttp_unused_port()})

    # target = os.path.join(tmp_dir, filename)
    target = filename
    assert not os.path.exists(target)

    my_json = {
        'filename': filename,
        'content': utils.JsonUtils.bytes2str(content),
    }
    resp = await client.post('/files', json=my_json)
    assert resp.status == HTTPStatus.OK
    resp_json = await resp.json()
    assert resp_json.get('status') == 'success'

    assert os.path.exists(target)
    with open(target, mode='rb') as f:
        new_content = f.read()
        assert content == new_content
