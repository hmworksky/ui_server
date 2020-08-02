from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from generate_data import models as gm
from common.response import Response


class SendView(APIView):

    def get(self, request, *args, **kwargs):
        """获取发送配置"""
        res = Response()
        send_type_list = list(gm.GenerateConf.objects.all().get("send_type"))
        print(send_type_list)
        return HttpResponse(send_type_list)

    def post(self, request, *args, **kwargs):
        """发送命令"""
        data = request.data
        print(data)
        print(data.get("high_blood_pressure"))
        return HttpResponse("ok")


