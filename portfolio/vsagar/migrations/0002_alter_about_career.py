# Generated by Django 3.2.3 on 2021-09-18 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vsagar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='career',
            field=models.CharField(max_length=50),
        ),
    ]
