# Generated by Django 4.0.2 on 2022-08-17 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catagories', '0004_alter_catagory_desc'),
        ('posts', '0003_alter_posts_catagory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='catagory',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='catagories.catagory'),
        ),
    ]
