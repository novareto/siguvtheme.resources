# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

import grok
from grok import util

from .layout import ILayer

from megrok.pagetemplate import PageTemplate
from uvc.layout import viewlets
from uvc.layout.interfaces import IAboveContent
from uvc.layout.slots import managers, menuviewlets
from uvc.layout.slots.menuviewlets import DocumentActionsMenuViewlet
from uvc.layout.slots.menuviewlets import PersonalPreferencesViewlet
from uvc.tbskin.viewlets import Breadcrumbs
from uvcsite.viewlets import steps
from zope.component import getMultiAdapter, queryMultiAdapter
from zope.interface import Interface
from zope.viewlet.interfaces import IContentProvider


grok.templatedir('templates')


class Navigation(grok.ViewletManager):
    grok.name('siguv-nav')
    grok.context(Interface)


class PersonalPreferencesViewlet(PersonalPreferencesViewlet):
    grok.layer(ILayer)
    grok.require('zope.View')

    @property
    def name(self):
        return ""

    def getFooterViewlet(self):
        viewlets = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IContentProvider,
            'footermenu').getMenuItems()
        return viewlets


class PersonalPreferencesTemplate(PageTemplate):
    grok.view(PersonalPreferencesViewlet)
    grok.layer(ILayer)


class FavIcon(grok.Viewlet):
    grok.layer(ILayer)
    grok.viewletmanager(managers.Headers)
    grok.context(Interface)


class GlobalMenuViewlet(menuviewlets.GlobalMenuViewlet):
    grok.layer(ILayer)
    grok.viewletmanager(Navigation)
    grok.order(1)

    def application_url(self):
        return util.application_url(self.request, self.context)

    def quicklinks(self):
        menu = queryMultiAdapter((self.view.context, self.request, self.view),
                                 IContentProvider, 'quicklinks')
        if menu is not None:
            return menu.getMenuItems()
        return None


class GlobalMenuTemplate(PageTemplate):
    grok.layer(ILayer)
    grok.view(menuviewlets.GlobalMenuViewlet)


class NavigationTemplate(PageTemplate):
    grok.layer(ILayer)
    grok.view(GlobalMenuViewlet)


class BGHeader(viewlets.header.BGHeader):
    grok.layer(ILayer)
    grok.order(30)

    def application_url(self):
        return util.application_url(self.request, self.context)


class DocumentActionsTemplate(PageTemplate):
    grok.view(DocumentActionsMenuViewlet)
    grok.layer(ILayer)


class Breadcrumbs(Breadcrumbs):
    grok.layer(ILayer)
    template = None

    def available(self):
        return False

    def render(self):
        return None


class StepsProgressBar(steps.StepsProgressBar):
    grok.layer(ILayer)

    def available(self):
        return False


class DocumentTabs(grok.Viewlet):
    grok.viewletmanager(IAboveContent)
    grok.context(Interface)

    def tabs(self):
        menu = queryMultiAdapter((self.view.context, self.request, self.view),
                                 IContentProvider, 'extraviews')
        if menu is not None:
            return menu.getMenuItems()
        return None

    def update(self):
        self.actions = self.tabs()
