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

    NOTE: Need to add blood request history, however hospital id is serial, need fixing

    Response:  it's a json file. Includes:
    @param      status          200: Success request
                                500: Failure request due to database
                                201: Not enough blood
                                202: Blood group not exist
    If success:  
    @param      status          200
    @param      name            hname
    @param      phone           phone
    @param      blood_group     bloodgroup
    @param      amount          amount
    @param      register_date   day

    If fail due to not enough blood:
    @param      status          201
    @param      name            hname
    @param      register_date   day
    '''
    async def request_blood(self, request):
        data = await request.json()
        hname = data['h-name']
        address = data['h-address']
        phone = data['h-num']
        bloodgroup = data['blood_group']
        amount = float(data['donate_amount'])/1000
        email = data['h-email']

        today = date.today()
        day = today.strftime("%Y-%m-%d")

        success = addHospital(hname, address, email, phone)
        if(success == 1):
            success = requestBloodDB(bloodgroup, amount)
            if(success == 2):
                #success = addBloodRequestHistory()
                # --> can add blood request history o day
                resp = {"status":"200", "name":hname, "address": address, "phone":phone, "blood_group": bloodgroup, "amount":str(amount),"registration_date":day}
            elif(success == 0):
                resp = {"status":"202"}
            elif(success == 1):
                resp = {"status":"201", "name":hname, "address": address, "phone":phone, "blood_group": bloodgroup, "amount":str(amount),"registration_date":day}

            elif(success == -1):
                resp = {"status":"500"}    
        
        return web.json_response(data=resp,  content_type='application/json', dumps=json.dumps)

    '''
    This function is used to create new register_blood_donation whenever
    a donor register. It takes the user info and pass to a function for query
    First, add donor
    Second, add blood
    Third, add blood to blood group

    Response:  it's a json file. Includes:
    @param      status          200: Success registration
                                500: Failure registration due to database
                                201: Server got the request but donor's last donation was less than 3 months ago
    If success:  
    @param      status          200
    @param      name            fname
    @param      pid             pid 
    @param      phone           phone
    @param      blood_group     blood_group
    @param      amount          amount
    @param      register_date   day

    If fail due to less than 3 months:
    @param      status          200
    @param      name            fname
    @param      pid             pid 
    @param      register_date   day
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
                #resp = "Email {} Name {} blood {} amount {} successfull".format(email, fname, bloodgroup, amount)
                resp = {"status":"200", "name":fname, "pid": pid, "phone":phone, "blood_group": bloodgroup, "amount":str(amount),"registration_date":day}
                text = "Registration success"
            elif(success == 0):
                deleteBlood(pid, day)
                #resp = "Can not update BloodGroup DB with ID = {}".format(pid)
                resp = {"status":"500"}
        elif(success == -2):
            resp = {"status":"500"}
        elif(success == 0):
            resp = {"status":"500"}
        elif(success == -1):
            #resp = "Donor's last donation was less than 3 months ago. Cannot add"
            resp = {"status":"201", "name":fname, "pid": pid, "registration_date":day}
        return web.json_response(data=resp,  content_type='application/json', dumps=json.dumps)
