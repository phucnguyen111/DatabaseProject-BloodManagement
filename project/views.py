from aiohttp import web
import aiohttp_jinja2

@aiohttp_jinja2.template('index.html')
async def index(request):
    return {'name': 'Andrew', 'surname': 'Svetlov'}


@aiohttp_jinja2.template('register.html')
async def register(request):
    return {'name': 'Andrew', 'surname': 'Svetlov'}


@aiohttp_jinja2.template('request.html')
async def request(request):
    return {'name': 'Andrew', 'surname': 'Svetlov'}