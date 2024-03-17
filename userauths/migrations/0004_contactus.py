# Generated by Django 5.0.2 on 2024-03-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(default='email@abc.com', max_length=254)),
                ('address', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=15)),
                ('information', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
    ]