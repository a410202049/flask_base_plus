#!/usr/bin/python
# -*- encoding: utf-8 -*-
from app.controller.home.IndexView import HomeIndex, UserAPI

CONFIG = {
    'ENCODING': 'utf-8'
}

_app = None


def init_routing(app):
    print 'init app in routing'

    app.add_url_rule('/', view_func=HomeIndex.as_view('index', template_name='index.html'))
    app.add_url_rule('/users/<int:user_id>', view_func=UserAPI.as_view('user_api'))
