# Generated by Django 3.1.3 on 2021-04-12 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_auto_20210412_1838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Stars',
            new_name='Rating',
        ),
    ]
