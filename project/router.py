import aiohttp
from aiohttp import web
import json
from aiohttp.web import json_response

from DBQueriesPython.addDonorDB import addDonor
from DBQueriesPython.addBloodDB import addBlood
from DBQueriesPython.addToBloodGroupDB import addToBloodGroup
from DBQueriesPython.addHospitalDB import addHospital
from DBQueriesPython.addBloodRequestHistory import addBloodRequestHistory
from DBQueriesPython.requestBloodDB import requestBloodDB

from DBQueriesPython.deleteBloodDB import deleteBlood
from DBQueriesPython.deleteBloodRequestHistory import deleteBloodRequestHistory

from datetime import date


class Router:
    '''
    NOTE: Not used yet
    '''
    async def create_user(self, request):
        data = await request.json()
        fname = data['fname']
        lname = data['lname']
        # pid = data['pid']
        gender = data['gender']
        address = data['address']
        phone = data['phone']
        bloodgroup = data['blood_group']
        medicalRecord = data['medical_record']
        email = data['email']

        create_donor(fname + lname, gender, address, email,
                     phone, blood-group, medicalRecord)
        resp = "Email {} Name {} blood {}".format(email, fname, blood-group)
        return web.Response(text=resp)

    '''
    NOTE: Not used yet
    '''
    async def login(self, request):
        data = await request.json()
        fname = data['fname']
        lname = data['lname']
        resp = "PID {} Name {} Hospital {}".format(
            pid, fname + lname, hospital)
        return web.Response(text=resp)

    '''
    NOTE: Not used yet
    '''
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

        success = addHospital(hname, address, email, phone)
        if(success == 1):
            success = requestBloodDB(bloodgroup, amount)
        resp = "Email {} Name {} blood {} amount {}".format(
            email, hname, bloodgroup, amount)
        return web.Response(text=resp)

    '''
    This function is used to create new register_blood_donation whenever
    a donor register. It takes the user info and pass to a function for query
    First, add donor
    Second, add blood
    Third, add blood to blood group

    NOTE: - change type of response from text to json

    '''
    async def register_blood_donation(self, request):
        data = await request.json()
        fname = data['fname']
        pid = data['pid']
        gender = data['gender']
        address = data['address']
        phone = data['phone']
        bloodgroup = data['blood_group']
        amount = float(data['donate_amount'])/1000
        email = data['email']

        today = date.today()
        day = today.strftime("%Y-%m-%d")

        success = addDonor(pid, fname, gender, address, email, phone)

        (success, latest_date) = addBlood(pid, bloodgroup, amount)

        if(success == 1):
            success = addToBloodGroup(bloodgroup, amount)
            if(success == 1):
                resp = "Email {} Name {} blood {} amount {} successfull".format(email, fname, bloodgroup, amount)
            elif(success == 0):
                deleteBlood(pid, day)
                resp = "Can not update BloodGroup DB with ID = {}".format(pid)

        elif(success == -2):
            resp = "Database error in calcDiff"

        elif(success == 0):
            resp = "Can not update Blood DB with ID = {}".format(pid)
        elif(success == -1):
            resp = "Donor's last donation was less than 3 months ago. Cannot add"

        return web.Response(text=resp)
