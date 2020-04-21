import aiohttp
from aiohttp import web
import json

class Router:
    #@get_request_json
    async def get_users(self, request, request_json):
        return web.Response(text="get_user")

    #@get_request_json
    async def update_users(self, request, request_json):
        return web.Response(text="get_user")

    #@get_request_json
    async def create_user(self, request, request_json):
        return web.Response(text="get_user")

    #@get_request_json
    async def login(self, request, request_json):
        return web.Response(text="get_user")

    #@get_request_json
    async def check_login(self, request, request_json):
        username = request_json.get('username')
        email = request_json.get('email')
        login = "Hello,  {} of email {}".format(username, email)
        web.Response(text=login)