import asyncio

from aiohttp import web

async def index():
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    # 定义路径和访问方法
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    _runner = web.AppRunner(app)
    await _runner.setup()
    _site = web.TCPSite(
        _runner, "127.0.0.1", 8000
    )
    await _site.start()
    print('Server started at http://127.0.0.1:8000...')
    return _runner, _site

loop = asyncio.get_event_loop()
runner, site = loop.run_until_complete(init(loop))
try:
    loop.run_forever()
except KeyboardInterrupt as err:
    loop.run_until_complete(runner.cleanup())
























