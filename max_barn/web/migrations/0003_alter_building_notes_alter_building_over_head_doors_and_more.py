# Generated by Django 4.2.2 on 2023-07-29 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_customer_add_city_alter_customer_add_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='over_head_doors',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='over_head_height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='over_head_width',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='porch_length',
            field=models.IntegerField(blank=True, null=True, verbose_name='Porch Length'),
        ),
        migrations.AlterField(
            model_name='building',
            name='porch_width',
            field=models.IntegerField(blank=True, null=True, verbose_name='Porch Width'),
        ),
        migrations.AlterField(
            model_name='building',
            name='windows',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
