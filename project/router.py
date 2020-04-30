import aiohttp
from aiohttp import web
import json
from aiohttp.web import json_response


class Router:
    async def create_user(self, request):
        data = await request.json()
        fname = data['fname']
        lname = data['lname']
        birthday = data['birthday']
        pid = data['pid']
        gender = data['gender']
        address = data['address']
        phone = data['phone']
        blood_group = data['blood-group']
        hospital = data['hospital']

        resp = "PID {} Name {} Hospital {}".format(pid, fname, hospital)
        return web.Response(text=resp) 

    async def login(self, request):
        data = await request.json()
        fname = data['fname']
        lname = data['lname']
        resp = "PID {} Name {} Hospital {}".format(pid, name, hospital)
        return web.Response(text=resp) 

    async def check_login_user(self, request):
        data = await request.json()
        for key in data.keys():
            print("key: ", key)
        fname = data['fname']
        lname = data['lname']
        pid = data['pid']
        
        return json_response({'status': 'success', 'data': pid}, status=200)

    async def request_blood(self, request):
        hname = data['hname']
        haddress = data['haddress']
        hnum = data['hnum']
        bloodgroup = data['blood-group']
        amount = data['amount']
        req = "Hello {} hospital of address {} and phone {}. {} of blood group {} is available ".format(hname, haddress, hnum, amount, bloodgroup)
        return web.Response(text=req)
    
