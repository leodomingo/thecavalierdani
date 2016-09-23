from rest_framework import viewsets
from rest_framework import filters
from unicorn.models import Author, Article, Tag, ArticleImage
from .serializers import (AuthorSerializer,
                          ArticleSerializer, TagSerializer,
                          ArticleImageSerializer)
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas


class AuthorViewSet(viewsets.ModelViewSet):

    """ Author Resource """

    resource_name = 'authors'
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = (
        filters.SearchFilter,
        filters.DjangoFilterBackend,)
    search_fields = ('first_name', 'last_name',)
    filter_fields = ('academic_year', 'school')


class ArticleViewSet(viewsets.ModelViewSet):

    """ Article Resource """

    resource_name = 'articles'
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (
        filters.SearchFilter,
        filters.DjangoFilterBackend,)
    search_fields = ('headline', 'abstract', 'copy', 'tags',)
    filter_fields = ('authors', 'status', 'tags', 'created',)


class TagViewSet(viewsets.ModelViewSet):

    """ Tag Resource """

    resource_name = 'tags'
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('text', 'description')


class ArticleImageViewSet(viewsets.ModelViewSet):

    """ ArticleImage Resource """

    resource_name = 'article_images'
    queryset = ArticleImage.objects.all()
    serializer_class = ArticleImageSerializer
    filter_backends = (
        filters.SearchFilter,)
    search_fields = ('description',)


# For django-rest-swagger docs
@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Unicorn API')
    return response.Response(generator.get_schema(request=request))
