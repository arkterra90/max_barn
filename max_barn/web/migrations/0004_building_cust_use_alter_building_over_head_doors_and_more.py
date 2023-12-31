# Generated by Django 4.2.2 on 2023-07-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_building_notes_alter_building_over_head_doors_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='cust_use',
            field=models.TextField(blank=True, null=True, verbose_name='Customer Use Case:'),
        ),
        migrations.AlterField(
            model_name='building',
            name='over_head_doors',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantity of Over Head Doors'),
        ),
        migrations.AlterField(
            model_name='building',
            name='over_head_height',
            field=models.IntegerField(blank=True, null=True, verbose_name='Over Head Door Height'),
        ),
        migrations.AlterField(
            model_name='building',
            name='over_head_width',
            field=models.IntegerField(blank=True, null=True, verbose_name='Over Head Door Width'),
        ),
        migrations.AlterField(
            model_name='building',
            name='walk_doors',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantity of Walkin Doors'),
        ),
        migrations.AlterField(
            model_name='building',
            name='windows',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantity of Windows'),
        ),
    ]
