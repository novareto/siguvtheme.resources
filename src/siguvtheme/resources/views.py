import grok
from uvcsite.homefolder import views
from .layout import ILayer
import megrok.pagetemplate as pt
from zeam.form.layout import Form
from uvc.layout.forms.components import Wizard
from dolmen.forms.base import ApplicationForm

grok.templatedir('templates')


class Index(views.Index):
    grok.layer(ILayer)

    cssClasses = {'table': 'table table-hover'}


class WizardTemplate(pt.PageTemplate):
    grok.layer(ILayer)
    pt.view(Wizard)

#class FormTemplate(pt.PageTemplate):
#    grok.layer(ILayer)
#    pt.view(ApplicationForm)
