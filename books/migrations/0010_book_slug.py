# Generated by Django 4.1.5 on 2023-03-07 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
