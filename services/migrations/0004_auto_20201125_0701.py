# Generated by Django 3.1.3 on 2020-11-25 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20201124_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='list_info1',
            field=models.CharField(max_length=50),
        ),
    ]
