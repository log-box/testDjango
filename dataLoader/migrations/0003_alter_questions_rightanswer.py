# Generated by Django 3.2.7 on 2021-09-07 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataLoader', '0002_questionscomments_questionsreviewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='rightAnswer',
            field=models.CharField(max_length=70, verbose_name='Ответ'),
        ),
    ]