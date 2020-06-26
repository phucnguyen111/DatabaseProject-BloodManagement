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

@aiohttp_jinja2.template('success-request.html')
async def success_request(request):
    return {'status': 'success-request'}

@aiohttp_jinja2.template('fail-request.html')
async def fail_request(request):
    return {'status': 'fail-request'}

@aiohttp_jinja2.template('success-register.html')
async def success_register(request):
    return {'status': 'success-register'}

@aiohttp_jinja2.template('fail-register.html')
async def fail_register(request):
    return {'status': 'fail-register'}