# Generated by Django 3.2.7 on 2021-12-20 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='joining_date',
            field=models.DateField(null=True),
        ),
    ]
