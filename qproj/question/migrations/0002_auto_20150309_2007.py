# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=1000)),
                ('text', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(to='question.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='upd_date',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
