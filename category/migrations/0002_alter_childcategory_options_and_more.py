# Generated by Django 5.0.1 on 2024-01-27 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='childcategory',
            options={'verbose_name': '3 - Child Category', 'verbose_name_plural': '3 - Child Category'},
        ),
        migrations.AlterModelOptions(
            name='maincategory',
            options={'verbose_name': '1 - Main Category', 'verbose_name_plural': '1 - Main Category'},
        ),
        migrations.AlterModelOptions(
            name='parentcategory',
            options={'verbose_name': '2 - Parent Category', 'verbose_name_plural': '2 - Parent Category'},
        ),
    ]