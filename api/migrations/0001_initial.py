# Generated by Django 4.2.7 on 2023-11-07 15:50

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
            name='BlogPostSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=120)),
                ('category', models.CharField(choices=[('Classic', 'Classic'), ('Crime', 'Crime'), ('Horror', 'Horror'), ('Poetry', 'Poetry'), ('Romance', 'Romance'), ('Biography', 'Biography')], max_length=50)),
                ('is_available', models.BooleanField(default=True)),
                ('published', models.DateField()),
                ('iso', models.CharField(max_length=13)),
                ('templates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]