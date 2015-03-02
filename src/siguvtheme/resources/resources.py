# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2011 NovaReto GmbH

from fanstatic import Library, Resource, Group
from js.jquery import jquery
from uvc.siguvtheme.resources import css, js, pretty, inset

library = Library('bg.siguvtheme', 'static')
maincss = Resource(library, 'main.css', depends=[css])
mainjs = Resource(library, 'main.js', depends=[js, jquery])
tune = Group([maincss, pretty, inset, mainjs])
