# Generated by Django 3.1.3 on 2020-12-04 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_ad_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='Units',
            field=models.CharField(choices=[('marla', 'MARLA'), ('kanal', 'KANAL'), ('square_feet', 'SQUARE_FEET'), ('square_yards', 'SQUARE_YARDS')], default='MARLA', max_length=128),
        ),
    ]
