# Generated by Django 3.2.7 on 2021-09-17 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataLoader', '0015_auto_20210917_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionsthemescategory',
            name='themeOfQuestion',
        ),
        migrations.AddField(
            model_name='questionsthemescategory',
            name='themeOfQuestion',
            field=models.ManyToManyField(to='dataLoader.QuestionsThemes'),
        ),
    ]