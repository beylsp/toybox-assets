SHELL := /bin/bash # Use bash syntax

define HELP_TEXT
HTTP assets server
===

Usage:

> make setup          # Prepare dependencies
> make init           # Create database
> make develop        # Run the dev server

endef

export PIPENV_VENV_IN_PROJECT=1

ENVPATH=${VIRTUAL_ENV}
PIPENV=pipenv
SYSTEM_DEPENDENCIES=python3-dev libpq-dev sqlite3 python3-pip

ifeq ($(ENVPATH),)
  ENVPATH=.venv
endif

##
# Print help test
##
help:
	$(info ${HELP_TEXT})

##
# Prepare the project
##
setup:
	# Install missing dependencies
	if ! dpkg -s ${SYSTEM_DEPENDENCIES} &> /dev/null; then \
		sudo apt update && sudo apt install -y ${SYSTEM_DEPENDENCIES}; \
	fi

	# Install pipenv globally (also installs virtualenv)
	type pipenv &> /dev/null || sudo python3 -m pip install pipenv

	# Create virtual env folder, if not already in one
	if [ -z ${VIRTUAL_ENV} ]; then ${PIPENV} --three; fi

	# Install requirements into virtual env
	${PIPENV} install

##
# Create database
##
init:
	${PIPENV} run flask db upgrade

##
# Start the development server
##
develop:
	${PIPENV} run flask run

# Non-file make targets
.PHONY: help setup init develop