# Generated by Django 4.2.2 on 2023-08-07 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoextra',
            name='hobbie',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
