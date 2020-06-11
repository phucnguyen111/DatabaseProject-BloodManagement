from settings import BASE_DIR


def setup_static_routes(app):
    app.router.add_static('/css/', path=BASE_DIR / 'project' / 'templates'/'css', name='css')
    app.router.add_static('/images/',path=BASE_DIR / 'project' / 'templates'/'images', name='images')
    app.router.add_static('/js/',path=BASE_DIR / 'project' / 'templates'/'js', name='js')