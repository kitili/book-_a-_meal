# Generated by Django 3.2.8 on 2021-10-19 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_merge_0002_menus_owner_0002_photos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='photos',
        ),
        migrations.AlterField(
            model_name='menus',
            name='menu_image',
            field=models.ImageField(upload_to='images/menus/'),
        ),
    ]
