# Generated by Django 2.1.5 on 2022-03-24 14:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Quizker', '0022_auto_20220323_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='likes',
        ),
        migrations.AddField(
            model_name='quiz',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
