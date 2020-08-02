from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'user'
        verbose_name = verbose_name_plural = '用户信息表'


class App(models.Model):
    """启动的APP"""
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    package_name = models.CharField(max_length=50, blank=False)

    class Meta:
        managed = False
        db_table = "app"


class Page(models.Model):
    """App对应的页面"""
    app_name = models.ForeignKey(App, on_delete=models.CASCADE)
    page_name = models.CharField(max_length=50, blank=False)

    class Meta:
        managed = False
        db_table = "page"


class Element(models.Model):
    """元素"""
    LOCATION_TYPE = (
        (0, "image"),
        (1, "id"),
        (2, "xpath"),
        (3, "text"),
        (4, "name"),
        (5, "resource-id")
    )
    name = models.CharField(max_length=50, blank=False, null=True, default="")
    app_id = models.ForeignKey(App, on_delete=models.CASCADE)
    page_id = models.ForeignKey(Page, on_delete=models.CASCADE)
    find_type = models.IntegerField(choices=LOCATION_TYPE, blank=False, null=False)

    class Meta:
        managed = False
        db_table = "element"


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




