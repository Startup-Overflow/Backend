# Generated by Django 4.0.2 on 2022-08-24 13:14

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hashtag', '0003_delete_follow'),
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('entre', models.BooleanField(default=False)),
                ('mentor', models.BooleanField(default=False)),
                ('investor', models.BooleanField(default=False)),
                ('incubator', models.BooleanField(default=False)),
                ('partner', models.BooleanField(default=False)),
                ('job_seaker', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UsersType',
            fields=[
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('type', models.CharField(choices=[('Mentor', 'mentor'), ('Entreprenur', 'entreprenur'), ('Investor', 'Investor'), ('Incubator', 'incubator'), ('Schemes', 'schemes')], default=None, max_length=255)),
                ('desc', ckeditor.fields.RichTextField(blank=True, default=None)),
                ('phone', models.CharField(default=None, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skill_name', to='hashtag.hashtag')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'unique_together': {('username', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interest_name', to='hashtag.hashtag')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'unique_together': {('username', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hobby_name', to='hashtag.hashtag')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'unique_together': {('username', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following', models.ForeignKey(null=True, on_delete=users.models.superuser, related_name='followed_by', to=settings.AUTH_USER_MODEL)),
                ('username', models.ForeignKey(null=True, on_delete=users.models.superuser, related_name='follow_to', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'unique_together': {('username', 'following')},
            },
        ),
    ]
