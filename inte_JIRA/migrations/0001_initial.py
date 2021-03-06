# Generated by Django 3.1.4 on 2020-12-02 13:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountCredentials',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('initial_url', models.CharField(blank=True, max_length=64)),
                ('email', models.CharField(blank=True, max_length=64)),
                ('API_key', models.CharField(blank=True, max_length=128)),
            ],
        ),
    ]
