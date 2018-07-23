#!/usr/bin/python
# -*- encoding: utf-8 -*-


def async(f):
    import gevent
    from gevent import Greenlet

    def wrapper(*args, **kwargs):
        t = Greenlet.spawn(f, *args, **kwargs)
        gevent.joinall([t])
    return wrapper


def _send_email(ctx, mail, msg):
    try:
        from . import get_app
        with get_app().app_context():
            mail.send(msg)
    except Exception, e:
        # ignore
        ctx.log.ex(e.message)
        pass


@async
def _send_async_email(ctx, mail, msg):
    _send_email(ctx, mail, msg)


def send_warning_email(ctx, title, body, recipients):

    try:
        from flask_mail import Message
        from flask_mail import Mail
        from flask import current_app

        msg = Message(title, sender=current_app.config['MAIL_USERNAME'], recipients=recipients)
        msg.body = body

        mail = Mail()
        mail.init_app(current_app)

        _send_async_email(ctx, mail, msg)
    except Exception, ex:
        # ignore
        ctx.log.ex(ex.message)
        pass
