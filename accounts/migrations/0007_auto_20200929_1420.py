# Generated by Django 3.0.4 on 2020-09-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200927_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='images/userprofile.png', null=True, upload_to=''),
        ),
    ]
