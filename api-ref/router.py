import jwt
from utils.utils import *
import re  # regular expression helper
from constants.regex import USERNAME_REGEX, PASSWORD_REGEX, EMAIL_REGEX, NAME_REGEX, LOCATION_REGEX, URL_REGEX, \
    DATE_REGEX, PHONE_REGEX, RESET_CODE_REGEX, DATE_FORMAT
from constants.security import JWT_KEY
from constants.message import *
import random
from web3_python_sample.sample_web3_testnet.read_test import get_data
from web3_python_sample.sample_web3_testnet.sign_test import sign_up
import mongodb
import aiohttp
import json


class Router:

    # return a transaction for user to sign by sending hashed values
    @get_request_json
    async def get_users(self, request, request_json):
        payload = request_json.get('signed_data')
        public_key = request_json.get('public_key')
        try:
            user = mongodb.get_user(public_key)
            for txid in user['txids']:
                data = get_data(txid)
                if data['_signature'] == payload:

                    response_data = {
                        'message': ADD_USER,
                        'txid': txid,
                        'data': data
                    }
                    return success(response_data)
            return fail(INVALID_SIGNATURE)
        except Exception as ex:
            return fail(str(ex))

    @get_request_json
    async def update_users(self, request, request_json):
        public_key = request_json.get('public_key')
        #new_hashed_data = request_json.get('new_hashed_data')
        new_signed_data = request_json.get('new_signed_data')
        # hashed fields that user wants to change
        values = request_json.get('values')
        if (values is not None and public_key is not None and new_signed_data is not None):
            try:
                # scan in database to get the correct txid
                result = mongodb.get_user(public_key)
                if result is None:
                    return fail(ERROR_PUBLIC_KEY, 404)
                # hash the values and then verify if the hashed values match the new signature or not
                # if yes then we have proved that user owns the public key, and confirms the hashed fields as well
                #hashed_temp = hash_data(values)
                # hash the values to check if they match the new_hashed_data
                #if hashed_temp != new_hashed_data:
                #    return fail(INVALID_VALUES)
                #if verify_data(public_key, new_hashed_data, new_signed_data) == True:
                else:
                    # because when adding txid into the list, the newest is added at the first index
                    tx_id = result['txids'][0]
                    fields = get_data(tx_id)

                    new_data = {
                        'username': values['username'] if 'username' in values.keys()
                        and values['username'] == fields['_username'] else '',
                        'email': values['email'] if 'email' in values.keys()
                        and values['email'] == fields['_email'] else '',
                        #'abc': values['abc'] if 'abc' in values.keys()
                        #and values['abc'] == fields['abc'] else '',
                        'signature': new_signed_data
                    }

                    print('new data: ', new_data)
                    new_txid = sign_up(new_data) # push new to Ethereum
                    if new_txid is not None:
                        # add more txid into the mongodb
                        new_txids = [new_txid]
                        new_txids.extend(result['txids'])
                        mongodb.update_user(public_key, 'txids', new_txids)
                        # check if data is updated or not
                        #data = mongodb.get_user(public_key)
                        #print("After updating txid: ", data)
                        response_data = {
                            'message': UPDATE_USER
                        }

                        # we need to notify the 3rd party server that user update
                        async with aiohttp.ClientSession() as session:
                            async with session.post('http://0.0.0.0:8081/update', data=json.dumps(new_data)) as resp:
                                if resp.status == 200:
                                    #print(await resp.text())
                                    return success(response_data)
                                return fail("ERROR UPDATE", 500)
                    return fail(ERROR_WEB3, 500)
                return fail(INVALID_SIGNATURE)
            except Exception as ex:
                return fail(str(ex))
        else:
            return fail(INVALID_INPUT)

    # return a transaction for user to sign by sending hashed values
    @get_request_json
    async def create_user(self, request, request_json):
        sig = request_json.get('signed_data')
        username = request_json.get('hashed_username')
        email = request_json.get('hashed_email')
        public_key = request_json.get('public_key')
        payload = {
            'username': username,
            'email': email,
            'signature': sig
        }
        #print('signed payload: ', payload)
        # check if account has been set or not
        user = mongodb.get_user(public_key)
        #print('user: ', user)
        if user is not None:
            return fail(EXISTING_ACCOUNT)
        try:
            # call web3 to get tx for user to sign
            txid = sign_up(payload)
            #data = get_data(txid)
            #print('data from Ether: ', data)

            create_user_statement = {
                "public_key": public_key, "txids": [txid]
            }
            mongodb.create_user(create_user_statement)
            #print("transaction: ", txid)
            response_data = {
                'message': ADD_USER,
                'txid': txid  # send back txid if user wants to check
            }

            return success(response_data)
            # return success(data)
        except Exception as ex:
            return fail(str(ex))

    @get_request_json
    async def login(self, request, request_json):
        public_key = request_json.get('public_key')
        hashed_data = request_json.get('hashed_data')

        # call a function eg: searchInformation - call web3 to search and compare data sent by users
        # txid and public key is returned to the website (Eg: Facebook)
        # this needs to scan all txids mapping with a public key sent by user

        if public_key is not None and hashed_data is not None:
            try:
                # scan in database to get the correct txid
                result = mongodb.get_user(public_key)
                # loop through the array to get txid
                for element in result['txids']:
                    # collect input data from Ether using txid
                    data = get_data(element)
                    signature = data['_signature']
                    print('signature: ', signature)
                    # compare hash value, if equal then success
                    #if (verify_data(public_key, hashed_data, signature) == True):
                    if hashed_data == signature:
                        # generate token
                        # a random string for one-time token
                        nonce = sha(random_string(100))
                        token = jwt.encode(
                            payload={'token': nonce,
                                     'exp': get_expiration_date(3)},  # 3 minutes
                            key=JWT_KEY,
                            algorithm='HS256')
                        token = token.decode('utf-8')
                        # store in mongo to later check
                        mongodb.update_user(public_key, 'token', token)
                        response_data = {
                            'message': LOGIN_SUCCESS,
                            'token': token
                        }
                        return success(response_data)
                return fail(INVALID_SIGNATURE)
            except Exception:
                return fail(WRONG_USERNAME_PASS)
        else:
            return fail(INVALID_INPUT)

    @get_request_json
    async def check_token(self, request, request_json):
        request_token = request_json.get('token')
        public_key = request_json.get('public_key')
        token_signature = request_json.get('token_signature')

        try:
            token = jwt.decode(request_token, JWT_KEY, algorithms=['HS256'])
            old_token = jwt.decode(mongodb.get_user(public_key)[
                                   'token'], JWT_KEY, algorithms=['HS256'])
            if token['token'] != old_token['token']:
                return fail(INVALID_TOKEN, 401)
            else:
                # add verification token that is hashed and signed by the private key of user
                #verification = verify_data(
                #    public_key, request_token, token_signature)
                #if verification == True:  # if correct then we approve the token
                response_data = {
                    'message': CORRECT_TOKEN,
                }
                return success(response_data)
        except jwt.ExpiredSignatureError:  # this checks automatically the exp date passed in the 'exp' key-value
            return fail(EXPIRED_TOKEN, 401)
        except jwt.InvalidTokenError:
            return fail(INVALID_TOKEN, 401)

    @get_request_json
    async def check_login(self, request, request_json):
        username = request_json.get('username')
        public_key = request_json.get('public_key')
        email = request_json.get('email')

        try:
            if (username is not None and public_key is not None and email is not None):
                user = mongodb.get_user(public_key)
                latest_id = user['txids'][0]
                fields = get_data(latest_id)
                if hash_data(username) == fields['_username'] and hash_data(email) == fields['_email']:
                    # flag checks other optional fields
                    flag = True
                    for key in request_json.keys():
                        if key == 'abc':
                            if '_abc' in fields.keys():
                                flag = False if hash_data(key) != fields['_abc'] else True
                            else:
                                flag = False
                        if key == 'egh':
                            if '_egh' in fields.key():
                                flag = False if hash_data(key) != fields['_egh'] else True
                            else:
                                flag = False
                    print('flag: ', flag)
                    if flag == True:
                        response_data = {
                            'message': "CORRECT INFORMATION",
                        }
                        return success(response_data)
                    return fail({
                        'message': 'Incorrect value fields !!'
                    })
                return fail(WRONG_USERNAME_PASS)
            return fail(INVALID_INPUT)
        except Exception as ex:
            return fail(str(ex))
