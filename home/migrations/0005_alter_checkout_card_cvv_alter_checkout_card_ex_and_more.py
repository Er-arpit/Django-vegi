# Generated by Django 4.2.2 on 2023-06-19 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_zip_checkout_zip_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='card_cvv',
            field=models.TextField(max_length=4),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='card_ex',
            field=models.TextField(max_length=3),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='card_name',
            field=models.TextField(max_length=21),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='card_no',
            field=models.TextField(max_length=12),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='zip_code',
            field=models.TextField(max_length=8),
        ),
    ]
