# Generated by Django 3.1.7 on 2021-03-16 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='links_db',
            name='links_name',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='links_db',
            name='links_path',
            field=models.CharField(default='', max_length=300),
        ),
    ]
