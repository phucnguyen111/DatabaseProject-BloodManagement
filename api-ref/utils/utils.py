import hashlib
from functools import wraps
from json.decoder import JSONDecodeError
from errors import ApiBadRequest
from aiohttp.web import json_response
import jwt
from constants.security import JWT_KEY
from constants.message import FORBIDDEN, INVALID_TOKEN, EXPIRED_TOKEN, UNAUTHORIZED
import random
import string
import base64
from datetime import datetime, timedelta
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii
from base64 import b64decode

# an utility function for a response that is success


def success(response_data, **kwargs):
    return json_response({**kwargs, 'status': 'success', 'data': response_data}, status=200)

# an utility function for a response that is failed


def fail(message, response_code=400, **kwargs):
    response_data = {'message': message}
    return json_response({**kwargs, 'status': 'fail', 'data': response_data}, status=response_code)

# an example of hashing


def sha(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    m = hashlib.sha1()
    m.update(data)
    return m.hexdigest()

# check the request to see if it's in a proper format or not


def decode_request(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            request = await args[1].json()
            args = (args[0], request)
            return await func(*args, **kwargs)
        except JSONDecodeError:
            raise ApiBadRequest('Improper JSON format')
    return wrapper

# when we collect the data we check if it's json or not


def get_request_json(f):
    @wraps(f)
    async def wrapper(*args, **kwargs):
        try:
            request_json = await args[1].json()
            args = (args[0], args[1], request_json)
            return await f(*args, **kwargs)
        except JSONDecodeError:
            raise ApiBadRequest('JSON is required!!!')

    return wrapper

def random_string(stringLength):
    """Generate a random string with the combination of lowercase and uppercase letters """

    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

def get_expiration_date(minute):
    dt = datetime.now() + timedelta(minutes=minute)
    return dt

def key_gen():
    return RSA.generate(bits=4096)

def sign_data(keyPair, hash):
    signer = PKCS115_SigScheme(keyPair)
    signature = signer.sign(hash)
    return signature

def hash_data(msg):
    if msg is None:
        return None
    msg_bytes = str.encode(msg) # has to be bytes
    return SHA256.new(msg_bytes).hexdigest() # return hex value of the hash

def hashing(msg):
    if msg is None:
        return None
    msg_bytes = str.encode(msg) # has to be bytes
    return SHA256.new(msg_bytes) # return hex value of the hash

def verify_data(public_key, hash, signature):
    verifier = PKCS115_SigScheme(public_key)
    try:
        verifier.verify(hash, signature) # need to hash before verifying
        return True
    except:
        return False