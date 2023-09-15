# Generated by Django 4.2.2 on 2023-06-19 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_vlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=122)),
                ('lname', models.CharField(max_length=122)),
                ('username', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=122)),
                ('address2', models.CharField(max_length=122)),
                ('country', models.CharField(max_length=122)),
                ('state', models.CharField(max_length=122)),
                ('zip', models.TextField()),
                ('card_name', models.TextField()),
                ('card_no', models.TextField()),
                ('card_ex', models.TextField()),
                ('card_cvv', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
