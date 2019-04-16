# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-16 09:11
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('ar_id', models.AutoField(primary_key=True, serialize=False, verbose_name='文章ID')),
                ('title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='文章类容')),
                ('is_show', models.IntegerField(choices=[(1, '是'), (0, '否')], default=0, verbose_name='是否前端显示')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发布时间')),
                ('r_number', models.IntegerField(default=0, verbose_name='阅读数')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'db_table': 'zjm_article',
            },
        ),
        migrations.CreateModel(
            name='ArticleCat',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False, verbose_name='文章分类id')),
                ('cat_name', models.CharField(max_length=20, verbose_name='分类名称')),
                ('cat_image', models.ImageField(blank=True, default='', upload_to='cat/%Y/%m%d', verbose_name='分类图片')),
                ('is_show', models.IntegerField(choices=[(1, '是'), (0, '否')], default=0, verbose_name='是否显示')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '文章分类',
                'verbose_name_plural': '文章分类',
                'db_table': 'zjm_cat',
            },
        ),
        migrations.AlterUniqueTogether(
            name='articlecat',
            unique_together=set([('cat_name',)]),
        ),
        migrations.AddField(
            model_name='article',
            name='cat_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.ArticleCat', verbose_name='文章分类'),
        ),
    ]
