# Generated by Django 4.0.2 on 2022-08-23 13:00

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usertype_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype',
            name='desc',
            field=ckeditor.fields.RichTextField(blank=True, default=None),
        ),
    ]