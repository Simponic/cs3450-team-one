# Generated by Django 4.0.1 on 2022-02-10 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_unique_email_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='availability',
        ),
        migrations.CreateModel(
            name='WorkerAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(default=0)),
                ('start_hour', models.IntegerField(default=0)),
                ('start_minute', models.IntegerField(default=0)),
                ('end_hour', models.IntegerField(default=23)),
                ('end_minute', models.IntegerField(default=59)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.worker')),
            ],
        ),
    ]
