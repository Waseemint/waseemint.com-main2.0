# Generated by Django 5.0.1 on 2024-08-14 06:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_account_city_remove_account_shop_name'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RenameField(
            model_name='account',
            old_name='is_superadmin',
            new_name='is_superuser',
        ),
        migrations.AddField(
            model_name='account',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='user_groups', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='account',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='user_permissions', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
