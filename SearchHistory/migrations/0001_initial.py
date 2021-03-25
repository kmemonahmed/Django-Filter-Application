# Generated by Django 3.1.7 on 2021-03-24 19:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword_Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=20)),
                ('keyword', models.CharField(max_length=200)),
                ('used', models.CharField(max_length=200)),
                ('search_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('searched_from', models.CharField(max_length=100)),
                ('searched_via', models.CharField(max_length=100)),
            ],
        ),
    ]