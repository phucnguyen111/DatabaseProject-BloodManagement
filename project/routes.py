from views import index
from router import Router

def setup_routes(app):
    app.router.add_get("/", index)
    # router_instance = Router()
    # app.router.add_post('/post/login', router_instance.login)
    # app.router.add_post('/post/users', router_instance.create_user)
    # app.router.add_post('/post/get', router_instance.get_users)
    # app.router.add_post('/post/check_login', router_instance.check_login)