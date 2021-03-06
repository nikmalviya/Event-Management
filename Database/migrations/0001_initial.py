# Generated by Django 2.1.7 on 2019-03-25 01:59

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
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, max_length=150, primary_key=True, serialize=False)),
                ('addressline', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=150)),
                ('area', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('pincode', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Catering',
            fields=[
                ('id', models.AutoField(auto_created=True, max_length=150, primary_key=True, serialize=False)),
                ('contact_no', models.CharField(max_length=150)),
                ('cost', models.CharField(default='', max_length=150)),
                ('foodtype', models.CharField(choices=[('veg', 'Veg'), ('nonveg', 'Non-Veg')], max_length=10)),
                ('name', models.CharField(default='', max_length=150)),
                ('Addressline', models.CharField(default='', max_length=150)),
                ('street', models.CharField(default='', max_length=150)),
                ('area', models.CharField(default='', max_length=150)),
                ('city', models.CharField(default='', max_length=150)),
                ('state', models.CharField(default='', max_length=150)),
                ('pincode', models.CharField(default='', max_length=150)),
                ('country', models.CharField(default='', max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Decoration',
            fields=[
                ('id', models.AutoField(auto_created=True, max_length=150, primary_key=True, serialize=False)),
                ('contact_no', models.CharField(max_length=150)),
                ('cost', models.CharField(max_length=150)),
                ('name', models.CharField(default='Name of Venue', max_length=150)),
                ('Addressline', models.CharField(default='Enter Address', max_length=150)),
                ('street', models.CharField(default='Enter Street', max_length=150)),
                ('area', models.CharField(default='Enter Area', max_length=150)),
                ('city', models.CharField(default='Enter City', max_length=150)),
                ('state', models.CharField(default='Enter state', max_length=150)),
                ('pincode', models.CharField(default='Enter pincode', max_length=150)),
                ('country', models.CharField(default='country', max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(auto_created=True, max_length=150, primary_key=True, serialize=False)),
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
                ('id', models.AutoField(max_length=150, primary_key=True, serialize=False)),
                ('needprinted', models.BooleanField(default=False)),
                ('iscustomized', models.BooleanField(default=False)),
                ('event', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Database.Address')),
            ],
        ),
        migrations.CreateModel(
            name='MenuImage',
            fields=[
                ('id', models.AutoField(auto_created=True, max_length=150, primary_key=True, serialize=False)),
                ('image', models.ImageField(default='', upload_to='Menu')),
                ('catering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Database.Catering')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, max_length=150, primary_key=True, serialize=False)),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('contact', models.CharField(max_length=12, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, default='', upload_to='ProfilePics')),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'other')], max_length=10)),
                ('first_name', models.CharField(blank=True, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SoundSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, max_length=150, primary_key=True, serialize=False)),
                ('contact_no', models.CharField(max_length=150)),
                ('cost', models.CharField(max_length=150)),
                ('name', models.CharField(default='Name of Venue', max_length=150)),
                ('Addressline', models.CharField(default='Enter Address', max_length=150)),
                ('street', models.CharField(default='Enter Street', max_length=150)),
                ('area', models.CharField(default='Enter Area', max_length=150)),
                ('city', models.CharField(default='Enter City', max_length=150)),
                ('state', models.CharField(default='Enter state', max_length=150)),
                ('pincode', models.CharField(default='Enter pincode', max_length=150)),
                ('country', models.CharField(default='country', max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='venue',
            fields=[
                ('id', models.AutoField(auto_created=True, max_length=150, primary_key=True, serialize=False)),
                ('image', models.ImageField(default='', null=True, upload_to='venueimage')),
                ('capacity', models.CharField(max_length=150)),
                ('ac', models.CharField(choices=[('ac', 'A/C'), ('non-ac', 'Non A/c')], max_length=10)),
                ('contact_no', models.CharField(max_length=150)),
                ('cost', models.CharField(max_length=150)),
                ('name', models.CharField(default='Name of Venue', max_length=150)),
                ('Addressline', models.CharField(default='Enter Address', max_length=150)),
                ('street', models.CharField(default='Enter Street', max_length=150)),
                ('area', models.CharField(default='Enter Area', max_length=150)),
                ('city', models.CharField(default='Enter City', max_length=150)),
                ('state', models.CharField(default='Enter state', max_length=150)),
                ('pincode', models.CharField(default='Enter pincode', max_length=150)),
                ('country', models.CharField(default='country', max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Database.venue'),
        ),
    ]
