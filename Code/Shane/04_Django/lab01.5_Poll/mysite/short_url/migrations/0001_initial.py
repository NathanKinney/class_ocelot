# Generated by Django 2.0.6 on 2018-06-28 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url', models.CharField(max_length=50)),
                ('long_url', models.CharField(max_length=3000)),
            ],
        ),
    ]
