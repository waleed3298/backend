# Generated by Django 3.1.3 on 2021-04-13 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_auto_20210412_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='Rating',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
