# Generated by Django 2.1.7 on 2019-03-10 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0004_auto_20190309_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='image',
            field=models.ImageField(blank=True, upload_to='venue image'),
        ),
    ]
