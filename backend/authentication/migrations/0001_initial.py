# Generated by Django 4.0.1 on 2022-02-04 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=255)),
                ('avatar', models.CharField(max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=16)),
                ('home_address', models.CharField(max_length=255, null=True)),
                ('home_latitude', models.FloatField(null=True)),
                ('home_longitude', models.FloatField(null=True)),
                ('balance', models.FloatField(default=0)),
                ('role', models.CharField(choices=[('owner', 'Owner'), ('customer', 'Customer'), ('worker', 'Worker')], default='customer', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, serialize=False, to='authentication.user')),
                ('availability', models.CharField(max_length=1024)),
            ],
        ),
    ]
