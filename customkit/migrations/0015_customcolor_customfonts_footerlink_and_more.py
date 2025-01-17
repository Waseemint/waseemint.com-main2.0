# Generated by Django 5.0.1 on 2024-08-14 06:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customkit', '0014_customproduct_discount_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CustomFonts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_fonts_link', models.TextField()),
                ('font_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('fontClass', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('allClasses', models.TextField(default='fb, googlePlus, pintrest, linkedin, insta, youtube, tiktok')),
            ],
        ),
        migrations.AddField(
            model_name='customproduct',
            name='images_five',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/custom_products_hover'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customproduct',
            name='images_four',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/custom_products_hover'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customproduct',
            name='images_three',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/custom_products_hover'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customorder',
            name='order_note',
            field=models.TextField(blank=True),
        ),
    ]
