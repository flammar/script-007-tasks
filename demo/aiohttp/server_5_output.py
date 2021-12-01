import csv
import json

from aiohttp import web


def to_json(obj):
    return json.dumps(obj, indent=2, sort_keys=True)


# test using curl:
# curl -v http://127.0.0.1/ -X GET -H "Content-Type: application/json"
# curl -v http://127.0.0.1/ -X GET -H "content-type: text/csv"
async def handle(request):

    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
    content_type = request.headers.get('Content-Type', 'text/plain')
    print(f'content_type = {content_type}')

    if content_type == 'application/json':
        data = {'some': 'data'}
        # https://docs.aiohttp.org/en/stable/web_quickstart.html#json-response
        return web.json_response(data)

    if content_type == 'text/plain':
        # https://docs.aiohttp.org/en/stable/web_reference.html#aiohttp.web.Response
        return web.Response(text='OK')

    if content_type == 'text/csv':
        content = """Id,Name
1,user1
2,user2
3,user3
"""
        headers = {'Content-Type': 'text/csv; charset=UTF-8'}
        return web.Response(
            body=content,
            headers=headers
        )

    # https://docs.aiohttp.org/en/stable/web_quickstart.html#exceptions
    raise web.HTTPBadRequest(text=f'unknown content type: {content_type}')


app = web.Application()
app.add_routes([
    web.get('/', handle),
])

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=80)
