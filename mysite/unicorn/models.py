from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=140)
    academic_year = models.IntegerField()
    school = models.CharField(max_length=40)

    def __str__(self):
        return '{first} {last}'.format(
            first=self.first_name, last=self.last_name)

    class Meta:
        ordering = ('last_name',)


class Tag(models.Model):
    text = models.SlugField(max_length=32, unique=True)
    description = models.CharField(max_length=140, default="")

    def __str__(self):
        return '{text}'.format(
            text=self.text)

    class Meta:
        ordering = ('text',)


class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=True)
    headline = models.CharField(max_length=100)
    abstract = models.TextField(max_length=100)
    authors = models.ManyToManyField(Author, related_name='articles')
    copy = models.TextField(max_length=300)
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=15)
    tags = models.ManyToManyField(Tag, related_name='articles')


    def add_author(self, new_author):
        self.authors.add(new_author)

    def add_tag(self, new_tag):
        self.tags.add(new_tag)

    def add_authors(self, author_list):
        for a in author_list:
            self.add_author(a)
        self.save()

    def add_tags(self, tag_list):
        for t in tag_list:
            self.add_tag(t)
        self.save()

    class Meta:
        ordering = ('created',)
