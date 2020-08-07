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


class AppElementSerializer(ModelSerializer):
    class Meta:
        model = um.AppElement
        fields = "__all__"
