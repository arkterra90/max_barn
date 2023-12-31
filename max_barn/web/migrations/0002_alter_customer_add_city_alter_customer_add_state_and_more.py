# Generated by Django 4.2.2 on 2023-07-29 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='add_city',
            field=models.CharField(max_length=64, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='add_state',
            field=models.CharField(choices=[('AR', 'Arkansas'), ('MO', 'Missouri'), ('OK', 'Oklahoma')], max_length=2, unique=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name_first',
            field=models.CharField(max_length=64, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name_last',
            field=models.CharField(max_length=64, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=16, verbose_name='Phone Number'),
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.IntegerField()),
                ('length', models.IntegerField()),
                ('height', models.IntegerField()),
                ('concrete', models.BooleanField(default=False)),
                ('color', models.CharField(choices=[('White', 'White'), ('Black', 'Black'), ('Light Gray', 'Light Gray'), ('Gray', 'Gray'), ('Dark Gray', 'Dark Gray'), ('Red', 'Red'), ('Maroon', 'Maroon'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Blue', 'Blue'), ('Purple', 'Purple'), ('Pink', 'Pink')], max_length=12)),
                ('trim', models.CharField(choices=[('White', 'White'), ('Black', 'Black'), ('Light Gray', 'Light Gray'), ('Gray', 'Gray'), ('Dark Gray', 'Dark Gray'), ('Red', 'Red'), ('Maroon', 'Maroon'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Blue', 'Blue'), ('Purple', 'Purple'), ('Pink', 'Pink')], max_length=20)),
                ('porch', models.BooleanField(default=False)),
                ('porch_concrete', models.BooleanField(default=False)),
                ('porch_length', models.IntegerField(verbose_name='Porch Length')),
                ('porch_width', models.IntegerField(verbose_name='Porch Width')),
                ('windows', models.IntegerField()),
                ('walk_doors', models.IntegerField()),
                ('over_head_doors', models.IntegerField()),
                ('over_head_height', models.IntegerField()),
                ('over_head_width', models.IntegerField()),
                ('notes', models.TextField()),
                ('plumbing', models.BooleanField(default=False)),
                ('cust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.customer')),
            ],
        ),
    ]
