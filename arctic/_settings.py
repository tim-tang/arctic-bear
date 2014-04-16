#!/usr/bin/env python

import os

# site information
SITE_TITLE = 'Arctic System'

# config for dev
DEBUG = True

# babel settings
BABEL_DEFAULT_LOCALE = 'zh'
BABEL_SUPPORTED_LOCALES = ['zh', 'en']

# static folder sttings
ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
if os.path.exists('static'):
    STATIC_FOLDER = os.path.join(os.getcwd(), 'static')
else:
    STATIC_FOLDER = os.path.join(ROOT_FOLDER, 'static')
