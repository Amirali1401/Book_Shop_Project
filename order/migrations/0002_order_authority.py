# Generated by Django 4.1.5 on 2023-04-14 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='authority',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
