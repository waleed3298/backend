# Generated by Django 3.1.1 on 2021-05-29 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0056_indices'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indices',
            old_name='value',
            new_name='index',
        ),
    ]
