# Generated by Django 3.0.1 on 2020-12-12 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('ename', models.CharField(max_length=30)),
                ('esalary', models.FloatField()),
                ('edept', models.CharField(max_length=30)),
            ],
        ),
    ]