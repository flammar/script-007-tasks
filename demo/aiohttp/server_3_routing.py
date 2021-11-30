from aiohttp import web


async def handle(request):
    # http://127.0.0.1/User
    name = request.match_info.get('name', 'Anonymous')
    text = f"Hello, {name}"
    return web.Response(text=text, content_type='text/html')


app = web.Application()
app.add_routes([
    web.get('/', handle),
    web.get('/{name}', handle),
])

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8080)
