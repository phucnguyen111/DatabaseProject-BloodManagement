import aiohttp
import json

class Router:
    @get_request_json
    async def get_users(self, request, request_json):
        return 1

    @get_request_json
    async def update_users(self, request, request_json):
        return 1

    @get_request_json
    async def create_user(self, request, request_json):
        return 1

    @get_request_json
    async def login(self, request, request_json):
        return 1

    @get_request_json
    async def check_login(self, request, request):
        username = request_json.get('username')
        email = request_json.get('email')
        try:
            if (username is not None and email is not None):
        except Exception as ex:
            return fail(str(ex))
