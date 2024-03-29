# Generated by Django 3.2.9 on 2024-01-20 11:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DOG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('objective_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('action_phrase', models.CharField(max_length=200)),
                ('number', models.IntegerField()),
                ('units', models.CharField(max_length=200)),
                ('deadline', models.DateTimeField(verbose_name='Dealine')),
                ('objective_type', models.CharField(choices=[('financial', 'financial'), ('non-financial', 'non-financial')], max_length=200)),
                ('priority', models.CharField(choices=[('High', 'High'), ('Low', 'Low')], max_length=200)),
                ('complexity', models.CharField(choices=[('Hard', 'Hard'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=200)),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('definition_of_good', models.ManyToManyField(to='objectives.DOG')),
            ],
        ),
    ]
