# Generated by Django 3.0.1 on 2020-12-11 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='adress',
            field=models.TextField(null=True),
        ),
    ]