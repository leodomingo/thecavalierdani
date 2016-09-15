from django.conf.urls import url

from . import views

from .forms import *
from .views import AuthorWizard, ArticleWizard

urlpatterns = [
    url(r'^$', views.articleList, name='Article List'),
    url(r'^dash$', views.dashboard, name='dashboard'),
    url(r'^(?P<slug>[\w-]+)/$', views.articleDetail, name='detail'),
    url(r'^author$', AuthorWizard.as_view(
        [AuthorForm1, AuthorForm2, AuthorForm3, AuthorForm4])),
    url(r'^article$', ArticleWizard.as_view(
        [ArticleForm1, ArticleForm2, ArticleForm4, ArticleForm5, ArticleForm6])),
]
