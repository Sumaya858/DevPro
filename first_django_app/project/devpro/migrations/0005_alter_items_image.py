# Generated by Django 4.2.3 on 2023-10-14 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devpro', '0004_items_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
