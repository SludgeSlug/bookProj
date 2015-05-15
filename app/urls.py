from django.conf.urls import patterns, include, static
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^helloworld/', include('helloworld.foo.urls')),

    # Hello, world!
    (r'^api/hello', 'app.views.index'),
    
    (r'^api/book', 'app.views.getBook'),

)

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
