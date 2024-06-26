# Generated by Django 4.2.11 on 2024-04-05 03:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('summary', models.CharField(max_length=60)),
                ('body', models.TextField(max_length=300)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='blog_pdfs/')),
                ('post_date', models.DateField(default=datetime.date.today)),
                ('slug', models.CharField(blank=True, max_length=1000, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
