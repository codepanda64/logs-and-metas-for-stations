# Generated by Django 3.0.3 on 2020-02-29 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='status',
            field=models.CharField(choices=[('selection', '勘选'), ('online', '在线'), ('suspend', '暂停'), ('offline', '下线')], default='selection', max_length=50, verbose_name='状态'),
        ),
    ]
