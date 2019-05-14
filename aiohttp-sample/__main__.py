from aiohttp import web

async def status(request):
    return web.json_response({'status': 'ok'})

if __name__ == '__main__':
    app = web.Application()
    app.router.add_get('/status', status)
    web.run_app(app)