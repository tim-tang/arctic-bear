# Author tim.tang
# Makefile for project Arctic
.PHONY: clean-pyc 

server:
	@python manager.py runserver

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +


# babel i18n
babel-extract:
	@python setup.py extract_messages -o messages.pot

language = zh
i18n = arctic/translations
babel-init:
	@python setup.py init_catalog -i messages.pot -d ${i18n} -l ${language}

babel-compile:
	@python setup.py compile_catalog -d ${i18n}

babel-update: babel-extract
	@python setup.py update_catalog -i messages.pot -d ${i18n}
