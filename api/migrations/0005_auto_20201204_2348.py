# Generated by Django 3.1.3 on 2020-12-04 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201204_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='Purpose',
            field=models.CharField(blank=True, choices=[('rent', 'RENT'), ('sale', 'SALE')], default='sale', max_length=128, null=True),
        ),
    ]
