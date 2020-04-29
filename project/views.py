from aiohttp import web
import aiohttp_jinja2

@aiohttp_jinja2.template('index.html')
async def index(request):
    # simplest view
    return {'name': 'Andrew', 'surname': 'Svetlov'}
    # create route for this


@aiohttp_jinja2.template('register.html')
async def register(request):
    fname =  request.match_info.get('fname')
    lname = request.match_info.get('lname')
    birthday = request.match_info.get('birthday')
    pid = request.match_info.get('pid')
    gender = request.match_info.get('gender')
    address = request.match_info.get('address')
    phone = request.match_info.get('phone')
    blood_group = request.match_info.get('blood_group')
    hospital = request.match_info.get('hosital')

    # code to add info to database
    # return register status 

    return {'name': 'Andrew', 'surname': 'Svetlov'}


@aiohttp_jinja2.template('request.html')
async def request(request):
    hname = request.match_info.get('h-name')
    haddress = request.match_info.get('h-address')
    hnum = request.match_info.get('h-num')
    bloodgroup = request.match_info.get('blood-group')
    amount = request.match_info.get('amount')
    # code to check info in database
    # return register status 

    return {'name': 'Andrew', 'surname': 'Svetlov'}