from viewshare.urls import *

from django.conf.urls import *
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
from django.views.generic.base import TemplateView
from viewshare.utilities.views import PlainTextResponse

urlpatterns += patterns('',

    # For legacy purposes
    url(r'^userupload/$', login_required(RedirectView.as_view(url="/upload")),
                                                              name="user_upload"),

    # Override the robots.txt template to
    (r'^robots.txt$', TemplateView.as_view(template_name="robots.txt",
                                           response_class=PlainTextResponse)),

    (r'^uservoice/', include('viewshare.apps.support.uservoice.urls')),

)