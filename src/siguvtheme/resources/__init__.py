# -*- coding: utf-8 -*-

import logging
from fanstatic import Library, Resource, Group
from js.jquery import jquery
from uvc.siguvtheme.resources import css, js, pretty, inset


library = Library('siguvtheme.resources', 'static')
maincss = Resource(library, 'main.css', depends=[css])
mainjs = Resource(library, 'main.js', depends=[js, jquery])
tune = Group([maincss, pretty, inset, mainjs])

logger = logging.getLogger('uvcsite.bg.siguvtheme')


def log(message, summary='', severity=logging.DEBUG):
    logger.log(severity, '%s %s', summary, message)

