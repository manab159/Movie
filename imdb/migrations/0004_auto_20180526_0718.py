# Generated by Django 2.0.5 on 2018-05-26 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0003_auto_20180526_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producers',
            name='DOB',
            field=models.DateField(),
        ),
    ]
