# Generated by Django 2.1.7 on 2019-05-24 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problem',
            old_name='submssions',
            new_name='submissions',
        ),
    ]
