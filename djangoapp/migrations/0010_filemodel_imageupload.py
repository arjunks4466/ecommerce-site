# Generated by Django 4.2.4 on 2023-10-12 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0009_regmodel_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='filemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='imageupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to='media')),
            ],
        ),
    ]
