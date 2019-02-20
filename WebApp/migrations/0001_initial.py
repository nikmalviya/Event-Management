# Generated by Django 2.1.7 on 2019-02-20 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=150, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_of_birthdate', models.DateField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]