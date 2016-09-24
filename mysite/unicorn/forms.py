from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Article, Author, Tag, ArticleAuthor, ArticleTag


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        exclude = ('created', 'edited',)


AuthorFormSet = inlineformset_factory(Author, ArticleAuthor,
                                      fields=('article',))
TagFormSet = inlineformset_factory(
    Tag, ArticleTag, exclude=('tag', 'article', 'test',))
