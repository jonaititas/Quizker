# Generated by Django 2.1.5 on 2022-03-17 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizker', '0010_auto_20220311_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trueorfalse',
            name='answer',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]