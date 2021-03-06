# Generated by Django 3.0.2 on 2020-02-24 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='台网代码')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='台网名称')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '测震台网信息',
                'verbose_name_plural': '测震台网信息',
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='台站代码')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='台站名称')),
                ('latitude', models.FloatField(default=0.0, verbose_name='纬度')),
                ('longitude', models.FloatField(default=0.0, verbose_name='经度')),
                ('altitude', models.FloatField(default=0.0, verbose_name='高程')),
                ('status', models.CharField(choices=[('selection', '勘选'), ('online', '在线'), ('suspend', '暂停'), ('offline', '下线')], default='online', max_length=50, verbose_name='状态')),
                ('selection', models.DateField(blank=True, null=True, verbose_name='勘选时间')),
                ('establish', models.DateField(blank=True, null=True, verbose_name='建台时间')),
                ('removal', models.DateField(blank=True, null=True, verbose_name='撤台时间')),
                ('remark', models.TextField(blank=True, verbose_name='备注')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stations', to='basicinfo.Network', verbose_name='台网')),
            ],
            options={
                'verbose_name': '测震台站信息',
                'verbose_name_plural': '测震台站信息',
                'ordering': ('network', 'code'),
                'unique_together': {('network', 'code')},
            },
        ),
        migrations.CreateModel(
            name='StationMoreInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo_desciription', models.TextField(blank=True, verbose_name='位置描述')),
                ('lithology_description', models.TextField(blank=True, verbose_name='岩性描述')),
                ('other_info', models.TextField(blank=True, verbose_name='其他信息')),
                ('station', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='more_info', to='basicinfo.Station')),
            ],
        ),
    ]
