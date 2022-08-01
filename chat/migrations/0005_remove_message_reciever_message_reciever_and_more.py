# Generated by Django 4.0.2 on 2022-02-28 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='reciever',
        ),
        migrations.AddField(
            model_name='message',
            name='reciever',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='GroupMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=256)),
                ('reciever', models.ManyToManyField(related_name='groupreciever', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ManyToManyField(related_name='groupsender', to='chat.GroupName')),
            ],
        ),
    ]
