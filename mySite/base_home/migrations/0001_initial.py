# Generated by Django 5.0.12 on 2025-02-18 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=50)),
                ('uname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('passwd', models.CharField(max_length=50)),
                ('birth', models.DateField()),
                ('telephn', models.IntegerField()),
            ],
        ),
    ]
