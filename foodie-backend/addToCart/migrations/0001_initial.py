# Generated by Django 3.1.6 on 2021-02-28 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddToCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubTotal', models.FloatField()),
                ('TotalBill', models.FloatField()),
                ('Dishes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dishes.dishes')),
            ],
        ),
    ]