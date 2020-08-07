from django.db import models
from ui.models import UserLogin


class UserDevice(models.Model):

    user = models.ForeignKey(UserLogin, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'user_device'
        verbose_name = verbose_name_plural = '设备管理'


class EnvManage(models.Model):
    name = models.CharField(max_length=20, default="test", blank=True, null=True)
    host = models.CharField(max_length=30, default="iotsbhjk.test.pajk.cn", blank=True, null=True)
    port = models.IntegerField(default=9999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'env_manage'
        verbose_name = verbose_name_plural = '环境管理'


class GenerateConf(models.Model):

    send_type = models.IntegerField(default=0, null=True, blank=True, help_text="发送类型")
    send_data_format = models.CharField(max_length=500, blank=False, help_text="发送格式")
    parameter = models.CharField(max_length=500, blank=False, null=True, help_text="发送参数")
    format_string = models.CharField(max_length=20, default="%s", null=True, blank=True, help_text="需要参数化的字符串")

    class Meta:
        db_table = 'generate_conf'
        verbose_name = verbose_name_plural = '发送配置'


class GenerateDataLog(models.Model):
    request_id = models.CharField(max_length=30, blank=False, null=False, help_text="请求ID")
    device = models.CharField(max_length=30, blank=False, null=False, help_text="设备号")
    env = models.CharField(max_length=30, null=True, default='test', help_text="环境")
    send_type = models.CharField(max_length=30, blank=False, null=False, default='heart', help_text="发送类型")
    message = models.CharField(max_length=200, blank=True, null=True, default='', help_text="发送的命令")
    status = models.IntegerField(default=0, help_text="状态，0：初始状态，1：已连接服务器，2：认证完成，3：发送命令完成")
    interval_time = models.IntegerField(default=10, help_text="发送间隔")
    send_count = models.IntegerField(default=1, help_text="发送总数")
    current_send_num = models.IntegerField(default=0, help_text="当前已发送数量")
    memo = models.CharField(max_length=2000, help_text="描述信息，错误信息等文案,前端展示文案")
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'generate_data_log'
        verbose_name = verbose_name_plural = '发送消息日志表'
