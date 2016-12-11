from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list, name="list"),
    url(r'^list/', views.list, name="list"),
    url(r'^write/', views.write, name="write"),
    url(r'^view/(?P<num>[0-9]+)/$', views.view, name="view"),
]