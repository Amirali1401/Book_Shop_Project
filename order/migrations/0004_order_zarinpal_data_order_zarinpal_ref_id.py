# Generated by Django 4.1.5 on 2023-04-23 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_rename_authority_order_zarinpal_authority'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='zarinpal_data',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='zarinpal_ref_id',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
