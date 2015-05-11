# -*- coding: utf-8 -*-

import logging
from fanstatic import Library, Resource, Group
from js.jquery import jquery

library = Library('siguvtheme.resources', 'static')

bootstrap_css = Resource(library, 'bootstrap_bundle.css', compiler='less', source='bootstrap_bundle.less')
siguv_css = Resource(library, 'siguv.css', compiler='less', source='siguv.less')


maincss = Resource(library, 'main.css', depends=[bootstrap_css, siguv_css])
mainjs = Resource(library, 'main.js', bottom=True)
siguvcss = Resource(library, 'siguvtheme.css')
tune = Group([maincss, siguvcss, mainjs])

logger = logging.getLogger('uvcsite.bg.siguvtheme')


def log(message, summary='', severity=logging.DEBUG):
    logger.log(severity, '%s %s', summary, message)
