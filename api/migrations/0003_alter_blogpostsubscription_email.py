# Generated by Django 4.2.7 on 2023-11-09 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostsubscription',
            name='email',
            field=models.EmailField(max_length=100, null=True, unique=True, verbose_name='email'),
        ),
    ]