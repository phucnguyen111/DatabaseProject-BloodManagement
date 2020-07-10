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
            context = {"request_status": "1", "name": hname, "address": address,
                       "phone": phone, "blood_group": bloodgroup, "amount": str(amount), "day": day}
            #resp = aiohttp_jinja2.render_template("success-request.html", request, context=context)
            #resp = web.Response("success-request.html")
            print('****** Request success')
            resp = web.json_response(
                data=context, content_type='application/json', dumps=json.dumps)
            #raise web.HTTPFound('/success-request.html')
        else:
            context = {"request_status": "0", "name": hname, "address": address,
                       "phone": phone, "blood_group": bloodgroup, "amount": str(amount), "day": day}
            #resp = aiohttp_jinja2.render_template("fail-request.html", request, context=context)
            #resp = web.Response("fail-request.html")
            print('****** Request fail')
            #raise web.HTTPFound('/fail-request.html')
            resp = web.json_response(
                data=context, content_type='application/json', dumps=json.dumps)
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

        if(addblood != 1):
            context = {"register_status": "0", "fname": fname, "pid": pid, "phone": phone,
                       "blood_group": bloodgroup, "amount": str(amount), "day": day}
            print('******  success')
            #raise web.HTTPFound('/fail-register.html')
            #resp = aiohttp_jinja2.render_template("fail-register.html", request, context=context)
            resp = web.json_response(
                data=context, content_type='application/json', dumps=json.dumps)
            print(' ==> render success')
        elif(addblood == 1):
            addtobloodgroup = addToBloodGroup(bloodgroup, amount)
            if(addtobloodgroup == 1):
                #resp = "Email {} Name {} blood {} amount {} successfull".format(email, fname, bloodgroup, amount)
                context = {"register_status": "1", "fname": fname, "pid": pid, "phone": phone,
                           "blood_group": bloodgroup, "amount": str(amount), "day": day}
                print('******  success')
                #raise web.HTTPFound('/success-register.html')

                #resp = aiohttp_jinja2.render_template("success-register.html", request, context=context)
                #resp = web.Response("success-register.html")
                resp = web.json_response(
                    data=context, content_type='application/json', dumps=json.dumps)
                print(' ==> render success')
            else:
                deleteBlood(pid, day)
                context = {"register_status": "0", "fname": fname, "pid": pid, "phone": phone,
                           "blood_group": bloodgroup, "amount": str(amount), "day": day}
                print('******  fail')
                #resp = aiohttp_jinja2.render_template("fail-register.html", request, context=context)
                #raise web.HTTPFound('/fail-register.html')
                print(' ==> render success')
                resp = web.json_response(
                    data=context, content_type='application/json', dumps=json.dumps)
                #resp = web.Response("fail-register.html")
        return resp

    '''
    This function returns the statistics of blood in json format

    '''
    async def show_statistic(self, request):
        Oplus_donor = '25'
        Oplus_amount = '6000' + ' ml'
        Ominus_donor = '25'
        Ominus_amount = '6000' + ' ml'

        Aplus_donor = '25'
        Aplus_amount = '6000' + ' ml'
        Aminus_donor = '25'
        Aminus_amount = '6000' + ' ml'

        Bplus_donor = '25'
        Bplus_amount = '6000' + ' ml'
        Bminus_donor = '25'
        Bminus_amount = '6000' + ' ml'

        ABplus_donor = '25'
        ABplus_amount = '6000' + ' ml'
        ABminus_donor = '25'
        ABminus_amount = '6000' + ' ml'

        resp = {'Oplus_donor': Oplus_donor, 'Oplus_amount': Oplus_amount,
                'Ominus_donor': Ominus_donor, 'Ominus_amount': Ominus_amount,
                'Aplus_donor': Aplus_donor, 'Aplus_amount': Aplus_amount,
                'Aminus_donor': Aminus_donor, 'Aminus_amount': Aminus_amount,
                'Bplus_donor': Bplus_donor, 'Bplus_amount': Bplus_amount,
                'Bminus_donor': Bminus_donor, 'Bminus_amount': Bminus_amount,
                'ABplus_donor': ABplus_donor, 'ABplus_amount': ABplus_amount,
                'ABminus_donor': ABminus_donor, 'ABminus_amount': Ominus_amount,}

        return json_response(resp, content_type='application/json', dumps=json.dumps)