# Generated by Django 4.1.5 on 2023-02-24 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('phone', models.CharField(max_length=30, verbose_name='Phone')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('address', models.CharField(max_length=80, verbose_name='Address')),
                ('company', models.CharField(max_length=30, verbose_name='Company')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Photo')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]