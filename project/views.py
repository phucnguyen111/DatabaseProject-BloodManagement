from aiohttp import web
import aiohttp_jinja2

@aiohttp_jinja2.template('index.html')
async def index(request):
    # simplest view
    return web.Response(text="Blood Management Application")
    # create route for this

