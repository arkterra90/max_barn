# Generated by Django 4.2.2 on 2023-07-29 19:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_customer_add_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
