# Generated by Django 3.1.3 on 2021-04-13 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0037_auto_20210413_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='Product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.product'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('user', 'Product')},
        ),
        migrations.AlterIndexTogether(
            name='review',
            index_together={('user', 'Product')},
        ),
        migrations.RemoveField(
            model_name='review',
            name='User',
        ),
    ]