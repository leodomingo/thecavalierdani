from rest_framework import serializers
from unicorn.models import Author, Article, Tag, ArticleImage


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article

    tags = TagSerializer(many=True)
    authors = AuthorSerializer(many=True)


class ArticleImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleImage
