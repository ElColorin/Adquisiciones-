# Generated by Django 4.1.2 on 2024-06-25 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Stock',
            new_name='stock',
        ),
    ]
