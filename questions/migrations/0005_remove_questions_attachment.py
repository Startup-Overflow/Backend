# Generated by Django 4.0.2 on 2022-08-19 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_alter_questions_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='attachment',
        ),
    ]
