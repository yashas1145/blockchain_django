# Generated by Django 3.2.18 on 2023-03-28 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=200)),
                ('hash', models.CharField(max_length=500)),
                ('prev_hash', models.CharField(max_length=500)),
            ],
        ),
    ]