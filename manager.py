#!/usr/bin/env python
# coding: utf-8

import os
from flask_script import Manager, Server
from arctic.app import create_app


settings = os.path.abspath('./etc/settings.py')

if 'ARCTIC_SETTINGS' not in os.environ and os.path.exists(settings):
    os.environ['ARCTIC_SETTINGS'] = settings

manager = Manager(create_app)
manager.add_option('-c', '--config', dest='config', required=False)
manager.add_command('runserver', Server())


@manager.command
def live(port=5000):
    from livereload import Server
    server = Server(manager.create_app())
    server.serve(port)

if __name__ == '__main__':
    manager.run()
