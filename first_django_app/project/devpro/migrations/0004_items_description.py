# Generated by Django 4.2.3 on 2023-09-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devpro', '0003_order_product_orderproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='description',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
