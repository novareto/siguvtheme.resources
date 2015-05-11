# -*- coding: utf-8 -*-

import logging
from fanstatic import Library, Resource, Group
from js.jquery import jquery


lessfiles = Library('uvc.siguvtheme', 'less')
css = Resource(lessfiles, 'bootstrap/css/siguvtheme.css', compiler='less', source='siguvtheme.less')
js = Resource(lessfiles, 'bootstrap/js/bootstrap.js')

pretty = Resource(lessfiles, 'bootstrap/js/google-code-prettify/prettify.css')
inset = Resource(lessfiles, 'assets/css/bootstrap-inset.css')

library = Library('siguvtheme.resources', 'static')
maincss = Resource(library, 'main.css', depends=[css])
mainjs = Resource(library, 'main.js', depends=[js, jquery])
tune = Group([maincss, pretty, inset, mainjs])

logger = logging.getLogger('uvcsite.bg.siguvtheme')


def log(message, summary='', severity=logging.DEBUG):
    logger.log(severity, '%s %s', summary, message)



