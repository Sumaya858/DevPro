# Generated by Django 4.2.3 on 2023-09-14 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devpro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wishtitle', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=1000)),
                ('image', models.CharField(max_length=500)),
            ],
        ),
    ]
