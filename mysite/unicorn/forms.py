from django import forms
from .models import Article, Author, Tag
from django.forms.formsets import BaseFormSet


class TagForm1(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['text']


class TagForm2(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['description']


class AuthorForm1(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class AuthorForm2(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['bio']


class AuthorForm3(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['academic_year', 'school']


class ArticleForm1(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['headline']


class ArticleForm2(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['abstract']


class ArticleForm3(forms.Form):
    if (len(Author.objects.all()) == 0):
        a = Author(first_name="Greatest", last_name="Ever")
        a.save()
    all_authors = Author.objects.all()
    authors = forms.ModelMultipleChoiceField(queryset=all_authors)


class ArticleForm4(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['copy']


class ArticleForm5(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['slug']


class ArticleForm6(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['status']


class ArticleForm7(forms.Form):
    if (len(Tag.objects.all()) == 0):
        t = Tag(text="uva")
        t.save()
    all_tags = Tag.objects.all()
    tags = forms.ModelMultipleChoiceField(queryset=all_tags)
