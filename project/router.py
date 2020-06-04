import aiohttp
from aiohttp import web
import json
from aiohttp.web import json_response

from db import create_donor
from DBQueriesPython.addNewBloodEntry import addNewBloodEntry
class Router:

    '''
    For blood group and medical record, _ doesnt work but - works
    '''
    async def create_user(self, request):
        data = await request.json()
        fname = data['fname']
        lname = data['lname']
        #pid = data['pid']
        gender = data['gender']
        address = data['address']
        phone = data['phone']
        bloodgroup = data['blood_group']
        medicalRecord = data['medical_record']
        email = data['email']

        create_donor(fname + lname, gender, address, email, phone, blood-group, medicalRecord)
        resp = "Email {} Name {} blood {}".format(email, fname, blood-group)
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

    '''
    This function process request_blood request from hospital
    It will call for an equivalent method to add to check from database
    NOTE: Havent been implemented to Database
    Temporarily okei
    '''
    async def request_blood(self, request):
        data = await request.json()
        hname = data['h-name']
        address = data['h-address']
        phone = data['h-num']
        bloodgroup = data['blood_group']
        amount = data['amount']
        email = data['h-email']

        #addNewBloodEntry(1, pid, fname, gender, address, email, phone, 123, amount, "Hello")
        resp = "Email {} Name {} blood {} amount {}".format(email, hname, bloodgroup, amount)
        return web.Response(text=resp) 
    
    '''
    This function is used to create new register_blood_donation whenever 
    a donor register. It takes the user info and pass to a function for query
    NOTE: Need modification according to fields in frontend
    Dang bia bua de test --> Run ok 
    '''
    async def register_blood_donation(self, request):
        data = await request.json()
        fname = data['fname']
        pid = data['pid']
        gender = data['gender']
        address = data['address']
        phone = data['phone']
        bloodgroup = data['blood_group']
        amount = data['donate_amount']
        email = data['email']

        addNewBloodEntry(1, pid, fname, gender, address, email, phone, 123, amount, "Hello")
        resp = "Email {} Name {} blood {} amount {}".format(email, fname, bloodgroup, amount)
        return web.Response(text=resp) 