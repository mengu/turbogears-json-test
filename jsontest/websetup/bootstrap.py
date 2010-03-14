# -*- coding: utf-8 -*-
"""Setup the json-test application"""

import logging
from tg import config
from jsontest import model

import transaction


def bootstrap(command, conf, vars):
    """Place any commands to setup jsontest here"""

    # <websetup.bootstrap.before.auth

    # <websetup.bootstrap.after.auth>
