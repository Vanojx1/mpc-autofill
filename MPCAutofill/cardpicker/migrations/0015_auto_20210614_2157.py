# Generated by Django 3.2.4 on 2021-06-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardpicker', '0014_auto_20210612_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='searchq_keyword',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cardback',
            name='searchq_keyword',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='token',
            name='searchq_keyword',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
