from django.conf.urls import url

from . import views

ARXIV_REGEXP = '([a-z\-\.]+\/[0-9]+|[0-9]{4}\.[0-9]{4,5})'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^comment/(?P<arXiv_id>%s)$' % ARXIV_REGEXP, views.comment),
    url(r'^list/(?P<arXiv_id>%s)$' % ARXIV_REGEXP, views.list),
    url(r'^user_info/$', views.user_info),
    url(r'^count_comments/$', views.count_comments),
]
