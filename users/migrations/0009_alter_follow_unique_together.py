# Generated by Django 4.0.2 on 2022-03-10 03:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_alter_hobbies_options_alter_interests_options_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('username', 'following')},
        ),
    ]
