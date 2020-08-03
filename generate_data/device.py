import socket
import time
import hashlib


class Device:

    def __init__(self, device, host=None):
        self.device = device
        self.host = host if host else "iotsbhjk.test.pajk.cn"
        self.port = 9999
        self.buf_size = 1024
        self.tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.status = 1
        self.result = []

    @property
    def sign(self):
        device_secret = self.device[-4:] + self.device[4:-4] + self.device[:4]
        product_id = "HJKGD01"
        conn_id = "test"
        expiry = int(time.time()) + 86400
        username = f"{product_id}{self.device};{conn_id};{expiry}"
        password = hashlib.md5(f"{username};{device_secret}".encode("UTF-8")).hexdigest()
        return f"IWAP00{self.device},{username},{password}#"

    def stop_receive(self):
        self.status = 0

    def close(self):
        """断开连接"""
        self.tcpCliSock.close()

    def connect(self):
        """连接服务器"""
        self.tcpCliSock.connect((self.host, self.port))

    def auth(self):
        """连接认证"""
        self.tcpCliSock.send(self.sign.encode())

    def send_message(self, data):
        """发送数据"""
        self.tcpCliSock.send(data.encode())

    def get_data(self):
        """获取数据"""
        while self.status:
            try:
                res = self.tcpCliSock.recv(self.buf_size)
                self.result.append(res)
            except Exception as e:
                self.status = 0

