# Generated by Django 3.0.5 on 2020-04-26 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0005_auto_20200425_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
