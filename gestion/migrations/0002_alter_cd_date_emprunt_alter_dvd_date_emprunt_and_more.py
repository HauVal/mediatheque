# Generated by Django 5.1.1 on 2024-09-23 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cd',
            name='date_emprunt',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='date_emprunt',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livre',
            name='date_emprunt',
            field=models.DateField(blank=True, null=True),
        ),
    ]
