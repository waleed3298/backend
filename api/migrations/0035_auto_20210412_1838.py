# Generated by Django 3.1.3 on 2021-04-12 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_auto_20210309_2258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Rating',
            new_name='Stars',
        ),
    ]
