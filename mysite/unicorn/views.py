from .models import Article, Author, Tag
from django.forms import modelformset_factory

from django.shortcuts import get_object_or_404, render, render_to_response

from formtools.wizard.views import SessionWizardView


def articleList(request):
    articleList = Article.objects.order_by('created')
    authorList = Author.objects.order_by('last_name')
    tagList = Tag.objects.order_by('text')
    context = {'articleList': articleList,
               'authorList': authorList, 'tagList': tagList}
    return render(request, 'unicorn/index.html', context)


def articleDetail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'unicorn/detail.html', {'article': article},)


def dashboard(request):
    ArticleFormSet = modelformset_factory(Article, exclude=())
    AuthorFormSet = modelformset_factory(Author, exclude=())
    TagFormSet = modelformset_factory(Tag, exclude=())
    if request.method == 'POST':
        articleformset = ArticleFormSet(request.POST, request.FILES)
        authorformset = AuthorFormSet(request.POST, request.FILES)
        tagformset = TagFormSet(request.POST, request.FILES)
        if articleformset.is_valid() and authorformset.is_valid() and tagformset.is_valid():
            tagformset.save()
            authorformset.save()
            articleformset.save()
            # do something.
        elif articleformset.is_valid() and authorformset.is_valid() and tagformset.is_valid():
            pass
    else:
        articleformset = ArticleFormSet()
        authorformset = AuthorFormSet()
        tagformset = TagFormSet()
    return render(request, 'unicorn/new.html',
                  {'articleformset': articleformset,
                   'authorformset': authorformset,
                   'tagformset': tagformset})


def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    return form_data

def flatten_dict(form_list):
    flattened_form_data = {}
    for elem in form_list:
        flattened_form_data.update(elem)
    return flattened_form_data



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
