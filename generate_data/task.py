from celery import task
from generate_data.device import Device


@task
def send_data(device, message):
    device_sock = Device(device)
    device_sock.connect()
    device_sock.auth()
    device_sock.send_message(message)
