# Generated by Django 5.0.12 on 2025-02-22 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_home', '0007_alter_payment_pdes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='birth',
        ),
        migrations.RemoveField(
            model_name='users',
            name='telephn',
        ),
    ]
