# -*- coding: utf-8 -*-

from application import app
from views import *
MODULES = (
    (public, ''),
    (projects, '/projects'),
)

def setting_modules(app, modules):
    """ 注册Blueprint模块 """
    for module, url_prefix in modules:
        app.register_blueprint(module, url_prefix=url_prefix)

setting_modules(app, MODULES)
