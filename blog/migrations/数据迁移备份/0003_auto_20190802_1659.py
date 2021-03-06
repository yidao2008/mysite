# Generated by Django 2.2.2 on 2019-08-02 16:59

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190802_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.AddField(
            model_name='post',
            name='contect',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='内空'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=250, unique_for_date='publish'),
        ),
    ]
