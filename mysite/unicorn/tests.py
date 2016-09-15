from django.test import TestCase
from .forms import *


class AuthorFormTests(TestCase):

    def test_author_form1_is_valid(self):
        form_data1 = {'first_name': u'foo', 'last_name': u'bar'}
        form = AuthorForm1(data=form_data1)
        self.assertTrue(form.is_valid())

    def test_author_form2_is_valid(self):
        form_data2 = {'bio': u'baz'}
        form = AuthorForm2(data=form_data2)
        self.assertTrue(form.is_valid())

    def test_author_form3_is_valid(self):
        form_data3 = {'academic_year': 2016}
        form = AuthorForm3(data=form_data3)
        self.assertTrue(form.is_valid())

    def test_author_form4_is_valid(self):
        form_data4 = {'school': u'seas'}
        form = AuthorForm4(data=form_data4)
        self.assertTrue(form.is_valid())
