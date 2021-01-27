# Generated by Django 2.2.15 on 2021-01-27 14:41

from django.db import migrations, models
import uploads.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('file', models.FileField(upload_to=uploads.models.upload_to)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]