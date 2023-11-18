# Generated by Django 4.2.4 on 2023-08-22 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0002_rename_email_register_email_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='registers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=30)),
                ('Last_name', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
