# Generated by Django 4.0.2 on 2022-08-19 14:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_unlikes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='desc',
            field=ckeditor.fields.RichTextField(),
        ),
    ]