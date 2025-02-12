# Generated by Django 5.1.1 on 2024-10-01 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='applied_position',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='candidate',
            name='applyingFor',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='candidate',
            name='currentCompany',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='candidate',
            name='currentLocation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='candidate',
            name='experience',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='candidate',
            name='firstName',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='candidate',
            name='jobType',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='candidate',
            name='lastName',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='candidate',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]
