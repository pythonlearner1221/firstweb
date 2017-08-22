from django.conf.urls import url

from .views import IndexView,ArchivesView,TagView,search

app_name='gifs'
urlpatterns=[
    url(r'^pics/$', IndexView.as_view(),name='gifs'),
    url(r'^pics/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',ArchivesView.as_view(),name='archives'),
    url(r'^pics/search/$',search,name='search'),
    url(r'^pictype/(?P<types>[a-z]+)/$',TagView.as_view(),name='tags'),
]