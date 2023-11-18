# Generated by Django 4.2.4 on 2023-08-31 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0007_audii'),
    ]

    operations = [
        migrations.CreateModel(
            name='stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('state', models.CharField(choices=[('Kerala', 'Kerala'), ('Tamilnadu', 'Tamilnadu'), ('Karnataka', 'Karnataka')], max_length=30)),
                ('english', models.BooleanField(default=False)),
                ('hindhi', models.BooleanField(default=False)),
                ('other', models.BooleanField(default=False)),
            ],
        ),
    ]