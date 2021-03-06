# Generated by Django 3.1.1 on 2021-05-24 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0052_auto_20210519_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
        migrations.AddField(
            model_name='blog',
            name='para1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='para2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='para3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='para4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='para5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='subheading1',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='subheading2',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='subheading3',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='subheading4',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
