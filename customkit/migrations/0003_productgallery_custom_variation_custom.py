# Generated by Django 5.0.1 on 2024-02-25 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customkit', '0002_alter_customproduct_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGallery_Custom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=255, upload_to='store/custom_products/')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='customkit.customproduct')),
            ],
            options={
                'verbose_name': 'productgallery',
                'verbose_name_plural': 'product gallery',
            },
        ),
        migrations.CreateModel(
            name='Variation_Custom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variation_category', models.CharField(choices=[('color', 'color'), ('size', 'size')], max_length=100)),
                ('variation_value', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customkit.customproduct')),
            ],
        ),
    ]