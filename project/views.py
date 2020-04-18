from aiohttp import web

async def index(request):
    # simplest view
    return web.Response(text="Blood Management Application")
    # create route for this