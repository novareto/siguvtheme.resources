# -*- coding: utf-8 -*-

import grok
from .resources import tune
from uvc.tbskin.skin import ITBSkin, Layout


grok.templatedir('templates')


class ILayer(grok.IDefaultBrowserLayer):
    pass


class ISkin(ILayer, ITBSkin):
    grok.skin('siguvtheme')


class MasterLayout(Layout):
    grok.name("")
    grok.layer(ILayer)

    def update(self):
        tune.need()
        Layout.update(self)
