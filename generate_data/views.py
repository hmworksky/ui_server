from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from generate_data import models as gm
from common.response import Response
from generate_data.task import send_data
from generate_data.message import Message


class SendView(APIView):

    def get(self, request, *args, **kwargs):
        """获取发送配置"""
        res = Response()
        send_type_list = list(gm.GenerateConf.objects.all().get("send_type"))
        print(send_type_list)
        return HttpResponse(send_type_list)

    def post(self, request, *args, **kwargs):
        """发送命令"""
        res = Response()
        data = request.data
        device = request.data.get("device")
        send_type = request.data.get("send_type")
        if not device:
            res['code'] = 1001
            res['message'] = '设备号不能为空'
        if not send_type:
            res['code'] = 1002
            res['message'] = '发送类型不能为空'
        message = getattr(Message, send_type)
        send_data.delay(device, message)
        return JsonResponse(res)


