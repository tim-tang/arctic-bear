# coding: utf-8

import arctic
from email.utils import parseaddr
from setuptools import setup, find_packages

kwargs = {}
try:
    from babel.messages import frontend as babel
    kwargs['cmdclass'] = {
        'extract_messages': babel.extract_messages,
        'update_catalog': babel.update_catalog,
        'compile_catalog': babel.compile_catalog,
        'init_catalog': babel.init_catalog,
    }
    kwargs['message_extractors'] = {
        'arctic': [
            ('**.py', 'python', None),
            ('**/templates/**.html', 'jinja2', {
                'extensions': (
                    'jinja2.ext.autoescape,'
                    'jinja2.ext.with_,'
                    'jinja2.ext.do,'
                )
            })
        ]
    }
except ImportError:
    pass

author, author_email = parseaddr(arctic.__author__)

setup(
    name='arctic',
    version=arctic.__version__,
    author=author,
    author_email=author_email,
    url='http://timtang.me/',
    packages=find_packages(exclude=['tests', 'tests.*']),
    license='MIT',
    zip_safe=False,
    include_package_data=True,
    **kwargs
)
