# Generated by Django 2.1.5 on 2022-03-10 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizker', '0005_rename_description_category_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('QuesitonType', models.CharField(max_length=256)),
            ],
        ),
    ]