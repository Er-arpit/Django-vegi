# Generated by Django 4.2.2 on 2023-06-19 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_checkout_card_cvv_alter_checkout_card_ex_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='zip_code',
            new_name='zipp',
        ),
    ]
