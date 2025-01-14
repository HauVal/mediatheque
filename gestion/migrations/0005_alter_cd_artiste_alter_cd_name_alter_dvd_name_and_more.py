# Generated by Django 5.1.1 on 2024-09-30 12:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_rename_emprunter_emprunt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cd',
            name='artiste',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='cd',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='realisateur',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='emprunt',
            name='date_emprunt',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='emprunteur',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='jeudeplateau',
            name='createur',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='jeudeplateau',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='livre',
            name='auteur',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='livre',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
