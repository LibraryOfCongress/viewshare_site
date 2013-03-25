from viewshare.urls import *

from django.conf.urls import *
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
from django.views.generic.base import TemplateView
from viewshare.utilities.views import PlainTextResponse

urlpatterns += patterns('',

    # URL mappings for fixed cms pages
    url(r'^tos/$', 'cms.views.details', kwargs={"slug": "tos"}, name="tos"),
    url(r'^about/community/$', 'cms.views.details', kwargs={"slug": "community"}, name="community"),
    url(r'^about/help/$', 'cms.views.details', kwargs={"slug": "help"}, name="help"),
    url(r'^about/faq/$', 'cms.views.details', kwargs={"slug": "faq"}, name="faq"),
    url(r'^about/userguide/$', 'cms.views.details', kwargs={"slug": "userguide"}, name="userguide"),
    url(r'^augment/patterns/$', 'cms.views.details', kwargs={"slug": "augment-list-patterns"}, name="augment-list-patterns"),

    # For legacy purposes
    url(r'^userupload/$', login_required(RedirectView.as_view(url="/upload")),
                                                              name="user_upload"),

    # Override the robots.txt template to
    (r'^robots.txt$', TemplateView.as_view(template_name="robots.txt",
                                           response_class=PlainTextResponse)),

    (r'^uservoice/', include('viewshare.apps.support.uservoice.urls')),

    # CMS url definition should come after all others
    (r'^', include('cms.urls')),
)