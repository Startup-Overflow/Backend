# Generated by Django 4.0.2 on 2022-08-18 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_posts_catagory'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='comment',
            field=models.IntegerField(default=0),
        ),
    ]