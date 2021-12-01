import json

from aiohttp import web


def to_json(obj):
    return json.dumps(obj, indent=2, sort_keys=True)


# test using curl:
# curl -v http://127.0.0.1/ -X GET --data "{\"param1\": 123,\"param2\":\"me!\"}"
async def handle(request):
    payload = ''
    stream = request.content
    while not stream.at_eof():
        line = await stream.read()
        payload += line.decode()
    print(f'raw input {payload}')

    # show pretty json
    data = json.loads(payload)
    print(f'pretty json\n{to_json(data)}')

    # show some fields
    param1 = data.get('param1')  # None by default
    param2 = data.get('param2', 'default_value2')
    print(f'param1: {param1}, param2: {param2}')

    return web.Response(text='OK')


app = web.Application()
app.add_routes([
    web.get('/', handle),
])

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=80)
