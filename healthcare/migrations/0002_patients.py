# Generated by Django 4.0.6 on 2022-09-03 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('treat_dept', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phonenum', models.IntegerField(default=0)),
                ('emailid', models.EmailField(max_length=254, unique=True)),
                ('bloodgroup', models.CharField(max_length=100)),
            ],
        ),
    ]
