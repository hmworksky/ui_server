from django_filters import rest_framework as rf
from ui import models as um


class AppFilter(rf.FilterSet):
    app_name = rf.CharFilter(field_name="app_name", lookup_expr="contains")
    package_name = rf.CharFilter(field_name="package_name", lookup_expr="contains")
    memo = rf.CharFilter(field_name="memo", lookup_expr="contains")

    class Meta:
        model = um.App
        fields = ["app_name", "package_name", "memo"]


class PageFilter(rf.FilterSet):
    app_name = rf.CharFilter(field_name="app_name", lookup_expr="contains")
    page_name = rf.CharFilter(field_name="page_name", lookup_expr="contains")

    class Meta:
        model = um.Page
        fields = ["app_name", "page_name"]


class AppElementFilter(rf.FilterSet):
    app_name = rf.CharFilter(field_name="app_name", lookup_expr="contains")
    page_name = rf.CharFilter(field_name="page_name", lookup_expr="contains")
    name = rf.CharFilter(field_name="name", lookup_expr="contains")
    find_type = rf.NumberFilter(field_name="find_type", lookup_expr="contains")

    class Meta:
        model = um.AppElement
        fields = ["name", "find_type", "app_name", "page_name"]