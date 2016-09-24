from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    headshot = models.ImageField(upload_to='headshots', blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=140)
    academic_year = models.IntegerField()
    SCHOOL_CHOICES = (
        ("SEAS", "School of Engineering and Applied Sciences"),
        ("BATTEN", "Frank Batten School of Leadership and Public Policy"),
        ("CLAS", "College of Arts and Sciences"),
        ("CURRY", "Curry School of Education"),
        ("Darden", "Darden School of Business"),
        ("COMM", "McIntire School of Commerce"),
        ("SARC", "School of Architecture"),
        ("SCPS", "School of Continuing and Professional Studies"),
        ("LAW", "School of Law"),
        ("MED", "School of Medicine"),
        ("NURSE", "School of Nursing"),
    )
    school = models.CharField(
        max_length=100,
        choices=SCHOOL_CHOICES)

    def __str__(self):
        return '{first} {last}'.format(
            first=self.first_name, last=self.last_name)

    class Meta:
        ordering = ('last_name',)


class Tag(models.Model):
    slug = models.SlugField(max_length=32, unique=True)
    description = models.CharField(max_length=140, default="")

    def __unicode__(self):
        return '%s: %s' % (self.slug, self.description)

    class Meta:
        ordering = ('slug',)


class ArticleImage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=140)
    image = models.ImageField(upload_to='images')


class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    headline = models.CharField(max_length=100)
    abstract = models.TextField(max_length=100)
    authors = models.ManyToManyField(Author, through='ArticleAuthor')
    copy = models.TextField(max_length=300)
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=15)
    tags = models.ManyToManyField(Tag, through='ArticleTag')
    images = models.ManyToManyField(ArticleImage, blank=True)


class ArticleTag(models.Model):
    """docstring for ArticleTag"""
    article = models.ForeignKey(Article)
    tag = models.ForeignKey(Tag)
    test = models.CharField(max_length=40, default='')


class ArticleAuthor(models.Model):
    """docstring for ArticleAuthor"""
    article = models.ForeignKey(Article)
    author = models.ForeignKey(Author)
