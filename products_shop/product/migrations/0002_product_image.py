# Generated by Django 4.0.6 on 2022-07-13 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Image',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
