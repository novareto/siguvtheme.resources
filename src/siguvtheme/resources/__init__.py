# -*- coding: utf-8 -*-

import logging
from fanstatic import Library, Resource, Group
#from js.jquery import jquery
#from uvc.siguvtheme.resources import css, js, pretty, inset


library = Library('siguvtheme.resources', 'static')
maincss = Resource(library, 'main.css')
mainjs = Resource(library, 'main.js', bottom=True)
siguvcss = Resource(library, 'siguvtheme.css')
tune = Group([maincss, siguvcss, mainjs])

logger = logging.getLogger('uvcsite.bg.siguvtheme')


def log(message, summary='', severity=logging.DEBUG):
    logger.log(severity, '%s %s', summary, message)
