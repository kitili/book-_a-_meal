# Generated by Django 3.2.8 on 2021-10-14 12:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='menus',
            fields=[
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('menu_image', models.ImageField(upload_to='menus/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
