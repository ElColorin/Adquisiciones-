# Generated by Django 4.1.2 on 2024-05-23 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
                ('Stock', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to='products')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sistema.category')),
            ],
        ),
    ]
