# Generated by Django 2.0.5 on 2018-05-26 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0002_auto_20180526_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genderchoice',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1, unique=True),
        ),
    ]
