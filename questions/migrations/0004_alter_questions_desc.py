# Generated by Django 4.0.2 on 2022-08-19 14:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_questions_answer_alter_answer_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='desc',
            field=ckeditor.fields.RichTextField(default=None),
        ),
    ]