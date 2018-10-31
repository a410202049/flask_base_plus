#!/usr/bin/python
# -*- encoding: utf-8 -*-

from app.controller.home import CommonView


class HomeBase(CommonView):

    def dispatch_request(self):
        context = {"school": {"name": "北京大学"}}
        context.update(self.render_data())
        return self.render_template(context)


class HomeIndex(HomeBase):

    def render_data(self):
        return {"student": {"name": "kerry"}}
