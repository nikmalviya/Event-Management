# Generated by Django 2.1.7 on 2019-02-21 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_auto_20190220_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.CharField(auto_created=True, max_length=150, primary_key=True, serialize=False)),
                ('addressline1', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=150)),
                ('area', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('pincode', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.CharField(auto_created=True, max_length=150, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('starttime', models.DateTimeField()),
                ('endtime', models.DateTimeField()),
                ('expected_people', models.CharField(max_length=150)),
                ('confirmed_people', models.CharField(max_length=150)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='invitation',
            fields=[
                ('id', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('needprinted', models.BooleanField(default=False)),
                ('iscustomized', models.BooleanField(default=False)),
                ('event', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='WebApp.events')),
            ],
        ),
        migrations.CreateModel(
            name='venue',
            fields=[
                ('id', models.CharField(auto_created=True, max_length=150, primary_key=True, serialize=False)),
                ('capacity', models.CharField(max_length=150)),
                ('ac', models.BooleanField(default=False)),
                ('contactno', models.CharField(max_length=150, unique=True)),
                ('cost', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='WebApp.venue'),
        ),
    ]