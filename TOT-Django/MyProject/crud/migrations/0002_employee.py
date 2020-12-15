# Generated by Django 3.0.1 on 2020-12-11 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empId', models.IntegerField()),
                ('efname', models.CharField(max_length=30)),
                ('elname', models.CharField(max_length=30)),
                ('edob', models.DateField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('eadress', models.TextField(max_length=30)),
                ('ephoto', models.ImageField(max_length=30, upload_to='')),
                ('eresume', models.FileField(max_length=30, upload_to='')),
                ('edesig', models.CharField(max_length=30)),
                ('esalary', models.IntegerField()),
            ],
        ),
    ]
