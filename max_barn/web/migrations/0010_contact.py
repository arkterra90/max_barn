# Generated by Django 3.2.12 on 2023-07-30 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_customer_zip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Price Shopping', 'Price Shopping'), ('Ready To Build', 'Ready To Build'), ('Future Build', 'Future Build')], max_length=20)),
                ('possible_build_date', models.DateTimeField()),
                ('site_details', models.TextField(verbose_name='Site Details')),
                ('on_site_appointment', models.DateTimeField()),
                ('made_contact', models.BooleanField(default=False)),
                ('notes', models.TextField()),
                ('cust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.customer')),
            ],
        ),
    ]
