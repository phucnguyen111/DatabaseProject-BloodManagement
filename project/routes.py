from views import index, register, request
from router import Router

def setup_routes(app):
    app.router.add_get("/", index)
    app.router.add_get("/index.html", index)
    app.router.add_get("/register", register)
    app.router.add_get("/register.html", register)
    app.router.add_get("/request", request)
    app.router.add_get("/request.html", request)

    router_instance = Router()
    app.router.add_post('/login', router_instance.login)
    app.router.add_post('/create_user', router_instance.create_user)
    app.router.add_post('/request_blood', router_instance.request_blood)
    app.router.add_post('/check_login_user', router_instance.check_login_user)
    app.router.add_post('/register_blood_donation', router_instance.register_blood_donation)
