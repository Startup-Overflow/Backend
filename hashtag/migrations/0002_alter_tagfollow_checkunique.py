# Generated by Django 4.0.2 on 2022-03-01 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashtag', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagfollow',
            name='checkunique',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
