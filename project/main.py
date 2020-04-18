from aiohttp import web

from router import Router
from routes import setup_routes
from settings import config
from db import close_pg, init_pg


app = web.Application(client_max_size=20*1024**2)
app['config'] = config

router_instance = Router()
app.router.add_post('/login', router_instance.login)
app.router.add_post('/users', router_instance.create_user)
app.router.add_post('/get', router_instance.get_users)
app.router.add_post('check_login', router_instance.check_login)

app.on_startup.append(init_pg)

for route in list(app.router.routes()):
    if not isinstance(route.resource, web.StaticResource):
        cors.add(route) 
app.on_cleanup.append(close_pg)
web.run_app(app, host='0.0.0.0', port='8080')
