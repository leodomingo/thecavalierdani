from .models import Article, Author, Tag
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, render, render_to_response
from formtools.wizard.views import SessionWizardView
from django.views.generic import ListView, DetailView


def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    return form_data


def flatten_dict(form_list):
    flattened_form_data = {}
    for elem in form_list:
        flattened_form_data.update(elem)
    return flattened_form_data


def getNewAuthor(data):
    new_author = Author(
        first_name=data['first_name'],
        last_name=data['last_name'],
        bio=data['bio'],
        academic_year=data['academic_year'],
        school=data['school'],
    )
    new_author.save()
    return new_author


def getNewTag(data):
    new_tag = Tag(
        text=data['text'],
        description=data['description'],
    )
    new_tag.save()
    return new_tag


class AuthorWizard(SessionWizardView):
    template_name = "unicorn/author_form.html"

    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        author_data = flatten_dict(form_data)
        new_author = Author(**author_data)
        new_author.save()
        return render_to_response('unicorn/done.html', {'form_data': form_data})


class ArticleWizard(SessionWizardView):
    template_name = "unicorn/article_form.html"

    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        article_data = flatten_dict(form_data)
        new_article = Article(
            headline=article_data['headline'],
            abstract=article_data['abstract'],
            copy=article_data['copy'],
            slug=article_data['slug'],
        )
        # Must save parent object before adding m2m relationships
        new_article.save()
        new_article.add_authors(article_data['authors'])
        new_article.add_tags(article_data['tags'])
        new_article.save()
        return render_to_response('unicorn/done.html', {'form_data': form_data})


class TagWizard(SessionWizardView):
    template_name = "unicorn/tag_form.html"

    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        new_tag = Tag(
            text=form_data[0]['text'],
            description=form_data[1]['description'],
        )
        new_tag.save()
        return render_to_response('unicorn/done.html', {'form_data': form_data})


class NewArticleWizard(SessionWizardView):
    template_name = "unicorn/new_article.html"

    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        article_data = flatten_dict(form_data)
        new_article = Article(
            headline=article_data['headline'],
            abstract=article_data['abstract'],
            copy=article_data['copy'],
            slug=article_data['slug'],
            status=article_data['status'],
        )
        # Must save parent object before adding m2m relationships
        new_article.save()

        new_article.add_authors(article_data['authors'])
        if (len(article_data['first_name']) > 0 and len(article_data['last_name']) > 0):
            new_author = getNewAuthor(article_data)
            new_article.add_author(new_author)

        new_article.add_tags(article_data['tags'])
        if (len(article_data['text']) > 0 and len(article_data['description']) > 0):
            new_tag = getNewTag(article_data)
            new_article.add_tag(new_tag)

        new_article.save()
        return render_to_response('unicorn/done.html', {'form_data': form_data})

class ArticleList(ListView):
    model = Article
    context_object_name = 'article_list'


class ArticleDetail(DetailView):
    model = Article


class AuthorList(ListView):
    model = Author
    context_object_name = 'author_list'


class AuthorDetail(DetailView):
    model = Author


class TagList(ListView):
    model = Tag
    context_object_name = 'tag_list'


class TagDetail(DetailView):
    model = Tag
