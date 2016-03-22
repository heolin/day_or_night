from django.conf.urls import patterns, url

urlpatterns = patterns('mainapp.views',
    url(r'^(?P<document_id>[0-9]+)/$', 'detail', name='detail'),
    url(r'^$', 'upload', name='upload'),
)
