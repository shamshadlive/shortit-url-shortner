# Generated by Django 4.2.7 on 2023-11-03 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=1000)),
                ('uuid', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]