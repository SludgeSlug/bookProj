from django.conf.urls import patterns, include, static
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^api/book', 'app.views.getBook'),
    (r'^api/quote', 'app.views.getQuote'),

)