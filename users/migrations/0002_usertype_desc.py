# Generated by Django 4.0.2 on 2022-08-23 12:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertype',
            name='desc',
            field=ckeditor.fields.RichTextField(blank=True, default='User'),
        ),
    ]