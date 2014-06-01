# coding: utf-8

import os
import datetime
import hashlib
import logging
from flask import Flask, render_template
from flask import g, request


def create_app(config=None):
    app = Flask(__name__, template_folder='templates',)

    app.config.from_pyfile('_settings.py')

    if 'ARCTIC_SETTINGS' in os.environ:
        app.config.from_envvar('ARCTIC_SETTINGS')

    if isinstance(config, dict):
        app.config.update(config)
    elif config:
        app.config.from_pyfile(os.path.abspath(config))

    app.static_folder = app.config.get('STATIC_FOLDER')
    app.config.update({'SITE_TIME': datetime.datetime.utcnow()})

    #register_jinja(app)
    #register_babel(app)
    register_routers(app)
    register_log(app)
    return app


def register_routers(app):
    from handlers import demo_handler
    #app.register_blueprint(demo_handler.bp, url_prefix='/demo')
    app.register_blueprint(demo_handler.bp)
    return app


def register_babel(app):
    """Configuration for Babel with i18n"""
    from flask_babel import Babel

    babel = Babel(app)
    supported = app.config.get('BABEL_SUPPORTED_LOCALES', ['en', 'zh'])
    default = app.config.get('BABEL_DEFAULT_LOCALE', 'en')

    @babel.localeselector
    def get_locale():
        return request.accept_languages.best_match(supported, default)


def register_jinja(app):

    if not hasattr(app, '_static_hash'):
        app._static_hash = {}

    def static_url(filename):
        if app.testing:
            return filename

        if filename in app._static_hash:
            return app._static_hash[filename]

        with open(os.path.join(app.static_folder, filename), 'r') as f:
            content = f.read()
            hsh = hashlib.md5(content).hexdigest()

        app.logger.info('Generate %s md5sum: %s' % (filename, hsh))
        prefix = app.config.get('SITE_STATIC_PREFIX', '/static/')
        value = '%s%s?v=%s' % (prefix, filename, hsh[:5])
        app._static_hash[filename] = value
        return value

    @app.context_processor
    def register_context():
        return dict(static_url=static_url,)

def register_log(app):
    """Track the logger in production environment."""
    if app.debug:
        return
    handler = logging.StreamHandler()
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)
