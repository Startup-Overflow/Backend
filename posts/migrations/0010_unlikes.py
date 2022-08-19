# Generated by Django 4.0.2 on 2022-08-18 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0009_alter_likes_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.posts')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('username', 'posts')},
            },
        ),
    ]