from django.test import TestCase
from .forms import *


class AuthorFormTests(TestCase):

    def test_author_form1_is_valid(self):
        form_data1 = {'first_name': u'Greatest', 'last_name': u'Ever'}
        form = AuthorForm1(data=form_data1)
        self.assertTrue(form.is_valid())

    def test_author_form2_is_valid(self):
        form_data2 = {'bio': u'The Six'}
        form = AuthorForm2(data=form_data2)
        self.assertTrue(form.is_valid())

    def test_author_form3_is_valid(self):
        form_data3 = {'academic_year': 2016, 'school': u'Ontario'}
        form = AuthorForm3(data=form_data3)
        self.assertTrue(form.is_valid())


class ArticleFormTests(TestCase):

    def test_article_form1_is_valid(self):
        form_data1 = {'headline': u'Honey'}
        form = ArticleForm1(data=form_data1)
        self.assertTrue(form.is_valid())

    def test_article_form2_is_valid(self):
        form_data2 = {'abstract': u'Nut'}
        form = ArticleForm2(data=form_data2)
        self.assertTrue(form.is_valid())

    # def test_article_form3_is_valid(self):
    #     author1 = Author(first_name="foo", last_name="bar")
    #     form_data3 = {'authors': author1}
    #     form = ArticleForm3(data=form_data3)
    #     self.assertTrue(form.is_valid())

    def test_article_form4_is_valid(self):
        form_data4 = {'copy': u'copypasta'}
        form = ArticleForm4(data=form_data4)
        self.assertTrue(form.is_valid())

    def test_article_form5_is_valid(self):
        form_data5 = {'slug': u'slug'}
        form = ArticleForm5(data=form_data5)
        self.assertTrue(form.is_valid())

    def test_article_form6_is_valid(self):
        form_data6 = {'status': u'status'}
        form = ArticleForm6(data=form_data6)
        self.assertTrue(form.is_valid())

    # def test_article_form6_is_valid(self):
    #     tag1 = Tag(text="text", description="description")
    #     form_data7 = {'tags': tag1}
    #     form = ArticleForm7(data=form_data7)
    #     self.assertTrue(form.is_valid())


def TagFormTests(TestCase):

    def test_tag_form1_is_valid(self):
        form_data1 = {'text': u'it\'s'}
        form = TagForm1(data=form_data1)
        self.assertTrue(form.is_valid())

    def test_tag_form2_is_valid(self):
        form_data2 = {'description': u'1am'}
        form = TagForm2(data=form_data)
        self.assertTrue(form.is_valid())
