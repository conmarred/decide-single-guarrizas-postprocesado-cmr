# Generated by Django 2.0 on 2021-01-04 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20180605_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionoption',
            name='genero',
            field=models.NullBooleanField(choices=[(True, 'Male'), (False, 'Female')]),
        ),
    ]
