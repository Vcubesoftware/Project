# Generated by Django 3.2.7 on 2021-12-06 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
