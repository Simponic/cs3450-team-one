# Generated by Django 4.0.1 on 2022-03-17 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0004_alter_worker_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.CharField(max_length=50)),
                ('icon', models.CharField(max_length=100)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('time_estimate', models.FloatField()),
                ('start_time', models.BigIntegerField(default=0)),
                ('end_time', models.BigIntegerField(default=0)),
                ('address', models.CharField(max_length=150)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('comment', models.CharField(max_length=150)),
                ('status', models.CharField(choices=[('available', 'Available'), ('assigned', 'Assigned'), ('complete', 'Complete'), ('disputed', 'Disputed')], default='available', max_length=15)),
                ('job_type', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobtype')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.user')),
            ],
        ),
    ]
