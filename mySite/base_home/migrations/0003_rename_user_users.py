# Generated by Django 5.0.12 on 2025-02-18 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_home', '0002_rename_member_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]
