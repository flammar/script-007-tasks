from aiohttp import web


async def handle(request):
    # http://127.0.0.1/?name=User
    params = request.rel_url.query
    name = params['name'] if 'name' in params else 'Anonimous!'
    text = "Hello, " + name
    return web.Response(text=text, content_type='text/html')


app = web.Application()
app.add_routes([
    web.get('/', handle),
])

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=80)
