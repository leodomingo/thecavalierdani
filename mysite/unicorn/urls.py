from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

from .forms import *

urlpatterns = [
    url(r'^new/*', views.ArticleCreateView.as_view()),
    url(r'^articles/$', login_required(views.ArticleList.as_view()),
        name='Article List'),
    url(r'^articles/(?P<slug>[-\w]+)/$',
        login_required(views.ArticleDetail.as_view()), name='Article Detail'),
    url(r'^tags/$', login_required(views.TagList.as_view()), name='Tag List'),
    url(r'^tags/(?P<slug>[-\w]+)/$',
        login_required(views.TagDetail.as_view()), name='Tag Detail'),
    url(r'^authors/$', login_required(views.AuthorList.as_view()),
        name='Author List'),
    url(r'^authors/(?P<pk>[-\w]+)/$',
        login_required(views.AuthorDetail.as_view()), name='Author Detail'),
]
