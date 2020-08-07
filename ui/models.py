from django.db import models

# Create your models here.


class UserLogin(models.Model):
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'user_login'
        verbose_name = verbose_name_plural = '用户信息表'


class App(models.Model):
    """启动的APP"""
    app_name = models.CharField(max_length=50, blank=False)
    package_name = models.CharField(max_length=50, blank=False)
    memo = models.CharField(max_length=2000, help_text="描述信息")
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        managed = False
        db_table = "app"


class Page(models.Model):
    """App对应的页面"""
    app_name = models.CharField(max_length=50, blank=False)
    page_name = models.CharField(max_length=50, blank=False)
    memo = models.CharField(max_length=2000, help_text="描述信息")
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        managed = False
        db_table = "page"


class AppElement(models.Model):
    """元素"""
    LOCATION_TYPE = (
        (0, "image"),
        (1, "by_id"),
        (2, "xpath"),
        (3, "text"),
        (4, "name"),
        (5, "resource_id")
    )
    element_name = models.CharField(max_length=30, blank=False, null=False, default="")
    memo = models.CharField(max_length=2000, null=True, blank=True, help_text="描述信息")
    app_name = models.CharField(max_length=30, blank=False, null=True, default="")
    page_name = models.CharField(max_length=30, blank=False, null=True, default="")
    find_type = models.IntegerField(choices=LOCATION_TYPE, blank=False, null=False)
    find_value = models.CharField(max_length=500, blank=False, null=True, default="")
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        managed = False
        db_table = "app_element"


class Process(models.Model):
    """流程"""
    name = models.CharField(max_length=50, blank=False, null=True, default="")
    app_id = models.ForeignKey(App, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = "process"


class Scene(models.Model):
    """场景"""
    name = models.CharField(max_length=50, blank=False, null=True, default="")
    process_id = models.ForeignKey(Process, on_delete=models.CASCADE)
    app_id = models.ForeignKey(App, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = "scene"




