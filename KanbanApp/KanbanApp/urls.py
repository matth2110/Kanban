"""
Definition of urls for KanbanProject.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import KanbanApp.forms
import KanbanApp.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', KanbanApp.views.home, name='home'),
    url(r'^contact$', KanbanApp.views.contact, name='contact'),
    url(r'^about', KanbanApp.views.about, name='about'),
    url(r'^tickets', KanbanApp.views.TicketListView.as_view(), name='tickets'),
    url(r'^createticket', KanbanApp.views.TicketCreateView.as_view(), name='createticket'),
    url(r'^login/$',
        django.contrib.auth.views.LoginView,
        {
            'template_name': 'app/login.html',
            'authentication_form': KanbanApp.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.LogoutView,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      url(r'^admin/', admin.site.urls),
]
