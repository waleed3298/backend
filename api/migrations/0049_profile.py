# Generated by Django 3.1.1 on 2021-05-04 23:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0048_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=128)),
                ('Gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], default='MALE', max_length=128)),
                ('Age', models.IntegerField(null=True)),
                ('CNIC', models.IntegerField(null=True)),
                ('Ad_quantity', models.IntegerField(default='4')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]