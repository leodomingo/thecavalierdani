from django import forms
from .models import Article, Author, Tag


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


class ArticleForm0(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['headline', 'abstract', 'copy', 'slug', 'status']
        exclude = ['authors', 'tags']


class AuthorForm0(forms.Form):
    if (len(Author.objects.all()) == 0):
        a = Author(last_name="Ever", first_name="Greatest")
        a.save()
    all_authors = Author.objects.all()
    authors = forms.ModelMultipleChoiceField(
        queryset=all_authors, required=False)

    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    bio = forms.CharField(max_length=140, required=False)
    academic_year = forms.IntegerField(required=False)
    school = forms.CharField(max_length=40, required=False)

    # Handles new author submission
    def cleaned_data(self):
        checkAuthor = self.cleaned_data.get('authors', '')
        checkNewAuthor = self.cleaned_data.get('first_name', 'academic_year')

        if not checkAuthor and not checkNewAuthor:
            raise forms.ValidationError("You must enter an author")

        if checkAuthor:
            return checkAuthor
        else:
            return checkNewAuthor


class TagForm0(forms.Form):
    if (len(Tag.objects.all()) == 0):
        t = Tag(text="uva")
        t.save()
    all_tags = Tag.objects.all()
    tags = forms.ModelMultipleChoiceField(queryset=all_tags, required=False)

    text = forms.SlugField(max_length=32, required=False)
    description = forms.CharField(max_length=140, required=False)

    # Handles new tag creation
    def cleaned_data(self):
        checkTag = self.cleaned_data.get('tags', '')
        checkNewTag = self.cleaned_data.get('text', '')

        if not checkTag and not checkNewTag:
            raise forms.ValidationError("You must enter a tag")

        if checkTag:
            return checkTag
        else:
            return checkNewTag
