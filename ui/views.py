from django.http.response import JsonResponse
from ui import models as um
from ui import filters as uf
from ui import serializers as us
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters as rf
from rest_framework import pagination
from django_filters.rest_framework import DjangoFilterBackend


class BasePagination(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = 'p'
    max_page_size = 200


class LimitPagination(pagination.LimitOffsetPagination):
    offset_query_param = 'offset'
    limit_query_param = 'limit'
    default_limit = 100
    max_limit = 1000


class BaseViewSet(ModelViewSet):
    pagination_class = BasePagination
    filter_backends = (DjangoFilterBackend, rf.SearchFilter, rf.OrderingFilter)
    ordering_fields = ("id", )


class AppViewSet(BaseViewSet):
    queryset = um.App.objects.all()
    serializer_class = us.AppSerializer
    filter_class = uf.AppFilter
    search_fields = ("name", "package_name")


class PageViewSet(BaseViewSet):
    queryset = um.Page.objects.all()
    serializer_class = us.PageSerializer
    filter_class = uf.PageFilter
    search_fields = ("app_name", "page_name")


class ElementViewSet(BaseViewSet):
    queryset = um.Element.objects.all()
    serializer_class = us.ElementSerializer
    filter_class = uf.ElementFilter
    search_fields = ("name", "find_type", "app_name", "page_name")

