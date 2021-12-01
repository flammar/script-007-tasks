import json
from aiohttp import web
class Handler:
    def __init__(self):
        print('ctor of Handler')
        
    async def root(self,request,*args,**keyargs):
        return web.Response(text = "Hello world")
    async def get_hello_for_name(self,request,*args,**keyargs):
        name = request.rel_url.query['name']
        return web.Response(text = 'Hello' + name)
    async def upload(self,request,*args,**keyargs):
        result = ''
        stream = request.content
        while not stream.at_eof():
           line = await stream.read()
           result += line.decode('utf-8')
    
        print(request.match_info('name'))    
        data = json.loads(result)
        print(data)
        print('----headers----')
        for i in request.headers.items():
            print(i)
        return web.json_response(data = {'status' : 'success'})
    async def get_info(self,request):
        print(request.match_info['name'])
        return web.Response(text = "ok")
        

app = web.Application()
handler = Handler()

app.add_routes([
    web.get('/', handler.root),
    web.get('/greet',handler.get_hello_for_name),
    web.post('/upload',handler.upload),
    web.get('/info/{name}',handler.get_info)
])
web.run_app(app)
