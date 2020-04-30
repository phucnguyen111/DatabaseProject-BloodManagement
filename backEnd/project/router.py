import aiohttp
from aiohttp import web
import json

class Router:
    async def get_users(self, request):
        return web.Response(text="get_user")

    async def update_users(self, request):
        return web.Response(text="get_user")

    async def create_user(self, request):
        return web.Response(text="get_user")

    async def login(self, request):
        return web.Response(text="get_user")


    async def check_login(self, request):
        return web.Response(text="get_user")