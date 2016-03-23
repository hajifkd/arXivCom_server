from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^comment/(?P<arXiv_id>.+)/$', views.comment),
    url(r'^list/(?P<arXiv_id>.+)/$', views.list),
    url(r'^user_info/$', views.user_info),
    url(r'^count_comments/$', views.count_comments),
]
