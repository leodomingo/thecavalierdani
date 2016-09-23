from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

from .forms import *
from .views import AuthorWizard, ArticleWizard, TagWizard, NewArticleWizard

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', views.articleDetail, name='detail'),
    url(r'^new/author$', AuthorWizard.as_view(
        [AuthorForm1, AuthorForm2, AuthorForm3])),
    url(r'^new/article$', ArticleWizard.as_view(
        [ArticleForm1, ArticleForm2, ArticleForm3, ArticleForm4, ArticleForm5, ArticleForm6, ArticleForm7])),
    url(r'^new/ta$', TagWizard.as_view([TagForm1, TagForm2])),
    url(r'^new$', NewArticleWizard.as_view(
        [ArticleForm0, AuthorForm0, TagForm0])),

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
