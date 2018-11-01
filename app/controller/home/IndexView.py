#!/usr/bin/python
# -*- encoding: utf-8 -*-
from flask import json

from app.controller.home import CommonView
from flask.views import MethodView

# from app.decorators.common_decorators import home_login_required


class HomeBase(CommonView):

    def dispatch_request(self):
        context = {"school": {"name": "北京大学"}}
        context.update(self.render_data())
        return self.render_template(context)


class HomeIndex(HomeBase):

    def render_data(self):
        return {"student": {"name": "kerry"}}


class UserAPI(MethodView):
    # decorators = [home_login_required]

    def get(self, user_id):
        return json.jsonify({"a": user_id})

    def post(self, user_id):
        return json.jsonify({"b": user_id})
