from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from generate_data import models as gm
from common.response import Response
from generate_data.tasks import send_data
from generate_data.message import Message


class SendDetailView(APIView):
    def get(self, request, *args, **kwargs):
        """获取发送详情"""
        res = Response()
        request_id = request.GET.get("request_id")
        first_db_obj = gm.GenerateDataLog.objects.filter(request_id=request_id).last()
        res["status"] = first_db_obj.status if first_db_obj else 0
        res["env"] = first_db_obj.env if first_db_obj else None
        res["device"] = first_db_obj.device if first_db_obj else None
        res["send_type"] = first_db_obj.send_type if first_db_obj else None
        res["log"] = []
        log_list = gm.GenerateDataLog.objects.filter(request_id=request_id).values("status", "memo", "update_time").order_by("-id")
        for log in log_list:
            _temp = {
                "status": log.get("status"),
                "memo": log.get("memo"),
                "update_time": log.get("update_time").strftime("%Y-%m-%d %H:%M:%S")
            }
            res["log"].append(_temp)
        return JsonResponse(res)


class SendView(APIView):

    def get(self, request, *args, **kwargs):
        """TODO 获取发送配置"""
        res = Response()

        request_id = request.GET.get("request_id")
        log_list = gm.GenerateDataLog.objects.filter(request_id=request_id).values(
            "device", "env", "status", "memo", "update_time")
        return HttpResponse(log_list)

    def post(self, request, *args, **kwargs):
        """发送命令"""
        res = Response()
        device = request.data.get("device")
        send_type = request.data.get("send_type")

        if not device:
            res['code'] = 1001
            res['message'] = '设备号不能为空'
        if not send_type:
            res['code'] = 1002
            res['message'] = '发送类型不能为空'
        message = getattr(Message, send_type)
        request_obj = request.data.dict()
        send_data.delay(request.data.dict(), message(**request_obj))
        return JsonResponse(res)


