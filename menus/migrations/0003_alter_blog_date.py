# Generated by Django 5.0.6 on 2024-06-18 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_alter_blog_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default='2021-09-01'),
        ),
    ]
