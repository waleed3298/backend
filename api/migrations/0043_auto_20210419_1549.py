# Generated by Django 3.1.3 on 2021-04-19 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_remove_orderitem_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='image',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='order',
            new_name='Order',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='price',
            new_name='Price',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='product',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='qty',
            new_name='Qty',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='brand',
            new_name='Brand',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='createdAt',
            new_name='CreatedAt',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='Price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='user',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='city',
            new_name='City',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='country',
            new_name='Country',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='order',
            new_name='Order',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='postalCode',
            new_name='PostalCode',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='shippingPrice',
            new_name='ShippingPrice',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='Name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Category',
            field=models.CharField(choices=[('electric', 'ELECTRIC'), ('paints', 'PAINTS'), ('wallpapers', 'WALLPAPERS'), ('construction_tools', 'CONSTRUCTION_TOOLS'), ('building_material', 'BUILDING_MATERIAL'), ('bathroom', 'BATHROOM'), ('lighting', 'LIGHTING'), ('hardware', 'HARDWARE'), ('decor', 'DECOR'), ('security', 'SECURITY'), ('kitchen', 'KITCHEN'), ('walls_and_flooring', 'WALLS_AND_FLOORING')], default='ELECTRIC', max_length=200),
        ),
    ]
