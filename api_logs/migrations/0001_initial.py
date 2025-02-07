# Generated by Django 4.2.13 on 2024-11-27 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APILog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(max_length=255)),
                ('request_data', models.TextField()),
                ('response_data', models.TextField()),
            ],
        ),
    ]
