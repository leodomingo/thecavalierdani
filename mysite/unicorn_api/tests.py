from rest_framework.test import APITestCase
from unicorn.models import Author, Article, Tag, ArticleImage
from django.core.urlresolvers import reverse
from rest_framework import status

# Create your tests here.


class GetAuthorTest(APITestCase):

    def setUp(self):
        data = {
            "headshot": "http://example.com",
            "first_name": "Bill",
            "last_name": "James",
            "bio": "Baseball dude",
            "academic_year": "4",
            "school": "The College of Arts and Sciences"
        }
        self.author = Author(**data)
        self.author.save()

    def test_can_get_author(self):
        response = self.client.get(
            reverse('author-detail', args=[self.author.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_get_author_list(self):
        response = self.client.get(reverse('author-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetArticleTest(APITestCase):

    def setUp(self):
        tag_data = {
            "description": "This is a test.",
            "slug": "helloworld"
        }
        article_image_data = {
            "description": "helloworld",
            "image": "http://example.com"
        }
        author_data = {
            "headshot": "http://example.com",
            "first_name": "Bill",
            "last_name": "James",
            "bio": "Baseball dude",
            "academic_year": "4",
            "school": "The College of Arts and Sciences"
        }
        tag = Tag(**tag_data)
        tag.save()
        article_image = ArticleImage(**article_image_data)
        article_image.save()
        author = Author(**author_data)
        author.save()
        data = {
            "headline": "Hello, world",
            "abstract": "asdfadf",
            "copy": "asdfasdf",
            "slug": "asdfads",
        }
        self.article = Article(**data)
        self.article.save()
        self.article.tags.add(tag)
        self.article.images.add(article_image)
        self.article.authors.add(author)

    def test_can_get_author(self):
        response = self.client.get(
            reverse('article-detail', args=[self.article.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_get_author_list(self):
        response = self.client.get(reverse('article-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetTagTest(APITestCase):

    def setUp(self):
        data = {
            "slug": "helloworld",
            "description": "This is a test"
        }
        self.tag = Tag(**data)
        self.tag.save()

    def test_can_get_author(self):
        response = self.client.get(
            reverse('tag-detail', args=[self.tag.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_get_author_list(self):
        response = self.client.get(reverse('tag-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetArticleImageTest(APITestCase):

    def setUp(self):
        data = {
            "description": "helloworld",
            "image": "http://example.com"
        }
        self.article_image = ArticleImage(**data)
        self.article_image.save()

    def test_can_get_author(self):
        response = self.client.get(
            reverse('article-image-detail', args=[self.article_image.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_get_author_list(self):
        response = self.client.get(reverse('article-image-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
