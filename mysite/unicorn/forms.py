from django import forms
from .models import Article, Author, Tag
from django.forms.formsets import BaseFormSet


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'bio', 'academic_year', 'school')


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ('text',)


class AuthorForm1(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)


class AuthorForm2(forms.Form):
    bio = forms.CharField(max_length=140)


class AuthorForm3(forms.Form):
    academic_year = forms.IntegerField()


class AuthorForm4(forms.Form):
    school = forms.CharField(max_length=40)


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
    authors = forms.ModelChoiceField(queryset=all_authors)


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
    tags = forms.ModelChoiceField(queryset=all_tags)
