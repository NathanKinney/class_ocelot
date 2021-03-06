# Generated by Django 2.0.6 on 2018-06-28 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_text', models.CharField(max_length=200)),
                ('due_date', models.DateTimeField(verbose_name='due date')),
                ('urgency', models.CharField(default='Meh', max_length=20)),
                ('created', models.DateField(default=django.utils.timezone.now)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created', models.DateField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TotoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyric', models.CharField(max_length=200)),
                ('song', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='todoitem',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoozer.TodoList'),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='toto_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoozer.TotoItem'),
        ),
    ]
