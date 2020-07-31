# Generated by Django 2.0.3 on 2020-07-31 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('package_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'app',
            },
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('find_type', models.IntegerField(choices=[(0, 'image'), (1, 'id'), (2, 'xpath'), (3, 'text'), (4, 'name'), (5, 'resource-id')])),
                ('app_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.App')),
            ],
            options={
                'db_table': 'element',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=50)),
                ('app_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.App')),
            ],
            options={
                'db_table': 'page',
            },
        ),
        migrations.AddField(
            model_name='element',
            name='page_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.Page'),
        ),
    ]
