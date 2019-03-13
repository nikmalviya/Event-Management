# Generated by Django 2.1.7 on 2019-03-10 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Database', '0005_venue_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoundSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, max_length=150, primary_key=True, serialize=False)),
                ('contact_no', models.CharField(max_length=150, unique=True)),
                ('cost', models.CharField(max_length=150)),
                ('name', models.CharField(default='Name of Venue', max_length=150)),
                ('Addressline', models.CharField(default='Enter Address', max_length=150)),
                ('street', models.CharField(default='Enter Street', max_length=150)),
                ('area', models.CharField(default='Enter Area', max_length=150)),
                ('city', models.CharField(default='Enter City', max_length=150)),
                ('state', models.CharField(default='Enter state', max_length=150)),
                ('pincode', models.CharField(default='Enter pincode', max_length=150)),
                ('country', models.CharField(default='country', max_length=150)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Database.Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='venue',
            name='image',
            field=models.ImageField(default='', null=True, upload_to='venueimage'),
        ),
    ]
