# Generated by Django 3.1.3 on 2021-04-19 15:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0044_auto_20210419_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='createdAt',
        ),
        migrations.AddField(
            model_name='order',
            name='createdAtDate',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='order',
            name='createdAtTime',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.order'),
        ),
    ]
