# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, request, redirect
from pylons.i18n import ugettext as _, lazy_ugettext as l_

from jsontest.lib.base import BaseController
from jsontest.model import DBSession, metadata
from jsontest.controllers.error import ErrorController

__all__ = ['RootController']


class RootController(BaseController):
    """
    The root controller for the json-test application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """

    error = ErrorController()

    @expose('json')
    def returnjson(self):
        pages = {'page': {'id': 1}}
        return pages

    @expose('jsontest.templates.test')
    def jsontest(self):
        return dict()

