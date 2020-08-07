from django.http.response import JsonResponse
from ui import models as um
from ui import filters as uf
from ui import serializers as us
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters as rf
from rest_framework import pagination
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from rest_framework.views import APIView


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


class AuthView(APIView):

    def post(self, request, *args, **kwargs):

        ret = {'code': 1000, 'msg': None}
        try:

            usr = request.data.get('username')
            pas = request.data.get('password')
            obj = um.UserLogin.objects.filter(username=usr, password=pas).first()
            if not obj:
                ret['code'] = '1001'
                ret['msg'] = '用户名或者密码错误'
                return JsonResponse(ret)
            ret['msg'] = '登录成功'
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求异常'
        print(ret)
        return JsonResponse(ret)


class AppViewSet(BaseViewSet):
    queryset = um.App.objects.all()
    serializer_class = us.AppSerializer
    filter_class = uf.AppFilter
    search_fields = ("app_name", "package_name")


class PageViewSet(BaseViewSet):
    queryset = um.Page.objects.all()
    serializer_class = us.PageSerializer
    filter_class = uf.PageFilter
    search_fields = ("app_name", "page_name")


class AppElementViewSet(BaseViewSet):
    queryset = um.AppElement.objects.all()
    serializer_class = us.AppElementSerializer
    filter_class = uf.AppElementFilter
    search_fields = ("name", "find_type", "app_name", "page_name")

