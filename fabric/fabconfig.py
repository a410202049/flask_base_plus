#!/usr/bin/python
# -*- coding:utf-8 -*-

environments = {
    "develop": {
        "hosts": ["xxxxx@xxxxxxxx:22"],
        "passwords": {"xxxx@xxxxxxxxx:22": "xxxx"},
        "colorize_errors": True,
        "project_name": "cqgcu_enroll_manager",
        "local_path": "../",
        "remote_path": "/home/xxxxxx/cqgcu_enroll_manager",
        "build": "docker build -t cqgcu-enroll-manager-nginx ./nginx && docker build -t cqgcu-enroll-manager .",
        "server_up": "docker-compose up -d",
        "server_stop": "docker-compose stop",
        "server_down": "docker-compose down",
        "server_ps": "docker-compose ps",
    },
}
