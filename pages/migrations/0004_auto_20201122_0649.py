# Generated by Django 3.1.3 on 2020-11-22 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20201122_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
