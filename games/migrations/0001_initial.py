# Generated by Django 2.1.2 on 2018-10-22 21:26

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('release_date', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1900), django.core.validators.MinValueValidator(2020)])),
            ],
        ),
    ]