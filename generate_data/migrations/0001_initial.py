# Generated by Django 2.1.3 on 2020-08-02 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ui', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnvManage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='test', max_length=20, null=True)),
                ('host', models.CharField(blank=True, default='iotsbhjk.test.pajk.cn', max_length=30, null=True)),
                ('port', models.IntegerField(blank=True, default=9999, max_length=30, null=True)),
            ],
            options={
                'verbose_name': '环境管理',
                'verbose_name_plural': '环境管理',
                'db_table': 'env_manage',
            },
        ),
        migrations.CreateModel(
            name='GenerateConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_type', models.IntegerField(blank=True, default=0, help_text='发送类型', max_length=20, null=True)),
                ('send_data_format', models.CharField(help_text='发送格式', max_length=500)),
                ('parameter', models.CharField(help_text='发送参数', max_length=500, null=True)),
                ('format_string', models.CharField(blank=True, default='%s', help_text='需要参数化的字符串', max_length=20, null=True)),
            ],
            options={
                'verbose_name': '发送配置',
                'verbose_name_plural': '发送配置',
                'db_table': 'generate_conf',
            },
        ),
        migrations.CreateModel(
            name='GenerateDataLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_type', models.CharField(help_text='发送类型', max_length=32)),
                ('message', models.CharField(help_text='发送的命令', max_length=500)),
                ('status', models.IntegerField(choices=[(0, 'success'), (1, 'info'), (2, 'error')], help_text='以什么状态打印日志')),
                ('memo', models.CharField(help_text='描述信息，错误信息等文案,前端展示文案', max_length=500)),
            ],
            options={
                'verbose_name': '发送消息日志表',
                'verbose_name_plural': '发送消息日志表',
                'db_table': 'generate_data_log',
            },
        ),
        migrations.CreateModel(
            name='UserDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.User')),
            ],
            options={
                'verbose_name': '设备管理',
                'verbose_name_plural': '设备管理',
                'db_table': 'user_device',
            },
        ),
        migrations.AddField(
            model_name='generatedatalog',
            name='device_id',
            field=models.ForeignKey(help_text='设备号', on_delete=django.db.models.deletion.CASCADE, to='generate_data.UserDevice'),
        ),
        migrations.AddField(
            model_name='generatedatalog',
            name='env_id',
            field=models.ForeignKey(help_text='环境', on_delete=django.db.models.deletion.CASCADE, to='generate_data.EnvManage'),
        ),
    ]
