# Generated by Django 2.0.5 on 2018-05-26 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0004_auto_20180526_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='year_of_release',
            field=models.PositiveIntegerField(default=2010),
        ),
    ]
