# Generated by Django 3.1.1 on 2021-05-24 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0053_auto_20210524_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='para6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='para7',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='subheading5',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='subheading6',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='subheading7',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]