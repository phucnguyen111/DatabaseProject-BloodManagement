import aiohttp
from aiohttp import web
import json
from aiohttp.web import json_response
import aiohttp_jinja2

from DBQueriesPython.addDonorDB import addDonor
from DBQueriesPython.addBloodDB import addBlood
from DBQueriesPython.addToBloodGroupDB import addToBloodGroup
from DBQueriesPython.addHospitalDB import addHospital
from DBQueriesPython.addBloodRequestHistory import addBloodRequestHistory
from DBQueriesPython.requestBloodDB import requestBloodDB

from DBQueriesPython.deleteBloodDB import deleteBlood
from DBQueriesPython.deleteBloodRequestHistory import deleteBloodRequestHistory

#from views import success_register, success_request, fail_register, fail_request
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
        amount = float(data['amount'])/1000
        email = data['h-email']

        today = date.today()
        day = today.strftime("%Y-%m-%d")

        addHos = addHospital(hname, address, email, phone)
        requestBlood = requestBloodDB(bloodgroup, amount)
        if(requestBlood == 2):
            #success = addBloodRequestHistory()
            # --> can add blood request history here
            context = {"request_status":"1", "name":hname, "address": address, "phone":phone, "blood_group": bloodgroup, "amount":str(amount),"day":day}
            resp = aiohttp_jinja2.render_template("success-request.html", request, context=context)
            return resp
        else:
            context = {"request_status":"0", "name":hname, "address": address, "phone":phone, "blood_group": bloodgroup, "amount":str(amount),"day":day}
            resp = aiohttp_jinja2.render_template("fail-request.html", request, context=context)
            return resp
        

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
        amount = data['donate_amount']
        amount = amount.replace("ml", "")
        amount = float(amount)/1000
        email = data['email']

        today = date.today()
        day = today.strftime("%Y-%m-%d")

        adddonor = addDonor(pid, fname, gender, address, email, phone)

        (addblood, latest_date) = addBlood(pid, bloodgroup, amount)

        if(addblood == 1):
            addtobloodgroup = addToBloodGroup(bloodgroup, amount)
            if(addtobloodgroup == 1):
                #resp = "Email {} Name {} blood {} amount {} successfull".format(email, fname, bloodgroup, amount)
                context = {"register_status":"1", "fname":fname, "pid": pid, "phone":phone, "blood_group": bloodgroup, "amount":str(amount),"day":day}
                resp = aiohttp_jinja2.render_template("success-register.html", request, context=context)
                return resp
            else:
                deleteBlood(pid, day)
                context = {"register_status":"0", "fname":fname, "pid": pid, "phone":phone, "blood_group": bloodgroup, "amount":str(amount),"day":day}
                resp = aiohttp_jinja2.render_template("fail-register.html", request, context=context)
                return resp
        else:
            context = {"register_status":"0", "fname":fname, "pid": pid, "phone":phone, "blood_group": bloodgroup, "amount":str(amount),"day":day}
            resp = aiohttp_jinja2.render_template("fail-register.html", request, context=context)
            return resp