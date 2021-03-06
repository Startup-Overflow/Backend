# Generated by Django 4.0.2 on 2022-03-10 13:39

from django.conf import settings
from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0009_alter_follow_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='username',
            field=models.ForeignKey(null=True, on_delete=users.models.superuser, related_name='follow_to', to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
