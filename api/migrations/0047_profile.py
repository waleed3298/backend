# Generated by Django 3.1.1 on 2021-05-04 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0046_orderitem_name'),
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
            ],
        ),
    ]
