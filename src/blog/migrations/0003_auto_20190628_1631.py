# Generated by Django 2.2 on 2019-06-28 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190628_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='context',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog_post',
            name='title',
            field=models.TextField(),
        ),
    ]
