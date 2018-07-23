#!/usr/bin/python
# -*- encoding: utf-8 -*-

import platform
CONFIG = {
    'SERVER_TYPE': '-',
    'SERVER_VERSION': '-',
    'SERVER_ID': '-',
    'SERVICE_ID': '-',
    'HOSTNAME': platform.node(),
    'VERSION': '-',
    'CONFIG_NAME': '-'
}


def init_app(app):
    if not app:
        return

    print 'init context app'
    for key in CONFIG.keys():
        if key in app.config:
            print 'set %s = %s' % (key, app.config[key])
            CONFIG[key] = app.config[key]
