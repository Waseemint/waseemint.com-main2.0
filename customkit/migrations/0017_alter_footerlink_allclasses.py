# Generated by Django 5.0.1 on 2024-08-20 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customkit', '0016_tags_remove_customorder_sizes_customorder_sizes_l_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footerlink',
            name='allClasses',
            field=models.TextField(default='fb, googlePlus, pintrest, linkedin, insta, youtube, tiktok,tw'),
        ),
    ]