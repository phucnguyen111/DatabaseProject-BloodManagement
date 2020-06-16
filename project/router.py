import aiohttp
from aiohttp import web
import json
from aiohttp.web import json_response

from db import create_donor

class Router:
    async def create_user(self, request):
        data = await request.json()
        fname = data['fname']
        lname = data['lname']
        #pid = data['pid']
        gender = data['gender']
        address = data['address']
        phone = data['phone']
        blood_group = data['blood-group']
        medicalRecord = data['medical-record']
        email = data['email']

        create_donor(fname + lname, gender, address, email, phone, blood_group, medicalRecord)
        resp = "Email {} Name {} blood {}".format(email, fname, blood_group)
        return web.Response(text=resp) 

    async def login(self, request):
        data = await request.json()
        fname = data['fname']
        lname = data['lname']
        resp = "PID {} Name {} Hospital {}".format(pid, fname + lname, hospital)
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
    
    async def register_blood_donation(self, request):
        data = await request.json()
        fname = data['fname']
        lname = data['lname']
        #pid = data['pid']  
        gender = data['gender']
        address = data['address']
        phone = data['phone']
        blood_group = data['blood-group']
        medicalRecord = data['medical-record']
        email = data['email']

        create_donor(fname + lname, gender, address, email, phone, blood_group, medicalRecord)
        resp = "Email {} Name {} blood {}".format(email, fname, blood_group)
        return web.Response(text=resp) 