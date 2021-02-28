# Generated by Django 3.1.6 on 2021-02-28 17:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deliver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliver_name', models.CharField(max_length=100)),
                ('deliver_password', models.CharField(max_length=50)),
                ('deliver_nidNo', models.IntegerField()),
                ('deliver_email', models.EmailField(max_length=62)),
                ('deliver_phoneNo', models.CharField(max_length=20)),
                ('deliver_accountCreated', models.DateTimeField(auto_now_add=True)),
                ('deliver_profilePicture', models.ImageField(blank=True, null=True, upload_to='')),
                ('deliver_dateOfBirth', models.DateTimeField()),
                ('deliver_address', models.TextField(max_length=200)),
                ('deliver_rating', models.FloatField(default=1.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
            ],
        ),
    ]
