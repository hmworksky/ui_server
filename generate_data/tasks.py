from celery import task
from generate_data.device import Device
from generate_data.models import GenerateDataLog as log
import time
from datetime import datetime


def save_message(**kwargs):
    log.objects.create(**kwargs)


@task
def send_data(request_param, message):
    memo = "准备开始连接服务器"
    print(f"params:{request_param}")
    device = request_param.get("device")
    request_id = request_param.get("request_id")
    send_count = int(request_param.get("send_count", 1))
    interval_time = int(request_param.get("interval_time", 20))
    db_data = {
        "memo": memo,
        "status": 0,
        "device": device,
        "message": message,
        "env": request_param.get("env"),
        "request_id": request_id,
        "send_count": send_count,
        "interval_time": interval_time,
        "send_type": request_param.get("send_type")
    }
    device_sock = Device(request_param.get("device"))
    try:
        device_sock.connect()
        db_data["memo"] = "连接成功"
    except Exception as e:
        db_data["memo"] = e
    db_data["status"] = 1
    save_message(**db_data)

    try:
        device_sock.auth()
        db_data["memo"] = "认证通过"
    except Exception as e:
        db_data["memo"] = e
    db_data["status"] = 2
    save_message(**db_data)

    time.sleep(3)

    db_data["memo"] = f"当前准备发送命令:{message}"
    db_data["status"] = 3
    save_message(**db_data)

    for num in range(send_count):
        device_sock.send_message(message)
        memo = f"当前正在发送第{num+1}个命令"
        log.objects.filter(request_id=request_id, status=3).update(memo=memo)
        time.sleep(interval_time/1000)

    db_data["memo"] = "发送完成"
    db_data["status"] = 4
    save_message(**db_data)
    device_sock.close()
