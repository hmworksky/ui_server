from ui import models as um
from rest_framework.serializers import ModelSerializer


class AppSerializer(ModelSerializer):
    class Meta:
        model = um.App
        fields = "__all__"


class PageSerializer(ModelSerializer):
    class Meta:
        model = um.Page
        fields = "__all__"


class ElementSerializer(ModelSerializer):
    class Meta:
        model = um.Element
        fields = "__all__"
