import asyncio
import logging

from aiohttp import web
import aiohttp_cors
from utils.utils import *
import rsa

from router import Router
import mongodb

logger = logging.getLogger(__name__)

app = web.Application(client_max_size=20*1024**2)
# WARNING: UNSAFE KEY STORAGE
# In a production application these keys should be passed in more securely
app['aes_key'] = 'ffffffffffffffffffffffffffffffff'
app['secret_key'] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
})

router_instance = Router()
app.router.add_post('/login', router_instance.login)
app.router.add_post('/users', router_instance.create_user)
app.router.add_post('/get', router_instance.get_users)
app.router.add_post('/update', router_instance.update_users)
app.router.add_post('/check_token', router_instance.check_token)
app.router.add_post('/check_login', router_instance.check_login)

for route in list(app.router.routes()):
        if not isinstance(route.resource, web.StaticResource):  # <<< WORKAROUND
            cors.add(route)

print(hash_data("this is test message") == "157e8f3c4022fbc2c54bd60f6f3d6c1c05a5d0118707dcf2b7b1a752d267cb54")

web.run_app(app, host="0.0.0.0", port="8080")
