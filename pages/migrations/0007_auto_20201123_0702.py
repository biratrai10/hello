# Generated by Django 3.1.3 on 2020-11-23 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20201123_0646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyheader',
            old_name='coimage',
            new_name='contact_image',
        ),
    ]
