from aiohttp import web
import aiohttp_jinja2

@aiohttp_jinja2.template('index.html')
async def index(request):
    return {'name': 'index'}


@aiohttp_jinja2.template('register.html')
async def register(request):
    return {'name': 'register'}


@aiohttp_jinja2.template('request.html')
async def request(request):
    return {'name': 'request'}

@aiohttp_jinja2.template('statistics.html')
async def statistic(request):
    return {'name': 'statistic'}