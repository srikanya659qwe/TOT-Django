# Generated by Django 3.0.1 on 2020-12-14 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondApp', '0002_emp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('ename', models.CharField(max_length=30)),
                ('edept', models.CharField(max_length=30)),
                ('esalary', models.FloatField()),
                ('isemployee', models.BooleanField(default=False, verbose_name='Is Employee')),
                ('isstudent', models.BooleanField(default=False, verbose_name='Is Student')),
                ('roles', models.CharField(choices=[('user', 'USER'), ('admin', 'ADMIN')], default='user', max_length=10)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=128)),
            ],
        ),
    ]
