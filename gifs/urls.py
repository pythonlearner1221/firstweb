from django.conf.urls import url

from .views import IndexView


app_name='gifs'
urlpatterns=[
    url(r'^gifs/', IndexView.as_view(),name='gifs')
]