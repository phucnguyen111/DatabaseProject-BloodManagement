from aiohttp import web
import aiohttp_jinja2
import jinja2

from router import Router
from routes import setup_routes
from settings import config, BASE_DIR
from db import close_pg, init_pg
from static import setup_static_routes

app = web.Application()
app['config'] = config

aiohttp_jinja2.setup(app,loader=jinja2.FileSystemLoader(str(BASE_DIR / 'project' / 'templates')))

setup_routes(app)
setup_static_routes(app)
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)

web.run_app(app,host="0.0.0.0", port="8081")
