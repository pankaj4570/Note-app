# Generated by Django 3.0.5 on 2020-04-23 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0002_auto_20200423_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.CharField(max_length=100),
        ),
    ]
