# Generated by Django 2.2.12 on 2021-06-27 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0005_auto_20210627_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
