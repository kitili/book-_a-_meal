# Generated by Django 3.2.8 on 2021-10-19 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_account_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_image',
            field=models.ImageField(blank=True, default='profiles/default.jpeg', null=True, upload_to='images/profiles'),
        ),
    ]