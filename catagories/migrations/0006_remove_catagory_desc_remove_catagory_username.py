# Generated by Django 4.0.2 on 2022-08-17 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catagories', '0005_alter_catagory_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catagory',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='catagory',
            name='username',
        ),
    ]
