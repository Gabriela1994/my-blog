# Generated by Django 4.0.4 on 2022-07-03 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favoritos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
