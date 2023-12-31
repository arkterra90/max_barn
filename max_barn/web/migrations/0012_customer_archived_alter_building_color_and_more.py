# Generated by Django 4.2.2 on 2023-07-30 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_remove_building_notes_remove_contact_notes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='building',
            name='color',
            field=models.CharField(choices=[('Black', 'Black STANDARD | PRIME | ULTRA'), ('Charcoal', 'Charcoal STANDARD | PRIME | ULTRA'), ('Pewter', 'Pewter PRIME'), ('Gray', 'Gray STANDARD | PRIME | ULTRA'), ('Alamo', 'Alamo STANDARD | PRIME | ULTRA'), ('Brilliant', 'Brilliant STANDARD | PRIME | ULTRA'), ('Forest', 'Forest STANDARD | PRIME | ULTRA'), ('Hunter', 'Hunter STANDARD | PRIME | ULTRA'), ('Colony', 'Colony PRIME'), ('Crimson', 'Crimson PRIME | ULTRA'), ('Deep Red', 'Deep Red PRIME'), ('Rustic', 'Rustic STANDARD | PRIME | ULTRA'), ('Burgundy', 'Burgundy STANDARD | PRIME | ULTRA'), ('Gallery', 'Gallery PRIME | ULTRA'), ('Ocean', 'Ocean PRIME | ULTRA'), ('Ivory', 'Ivory PRIME'), ('Light Stone', 'Light Stone STANDARD | PRIME | ULTRA'), ('Desert', 'Desert PRIME'), ('Copper Metallic', 'Copper Metallic*† PRIME'), ('Galvalume', 'Galvalume STANDARD | PRIME | ULTRA'), ('Burnished Slate', 'Burnished Slate STANDARD | PRIME | ULTRA'), ('Brown', 'Brown STANDARD | PRIME | ULTRA'), ('Tan', 'Tan STANDARD | PRIME | ULTRA'), ('Taupe', 'Taupe STANDARD | PRIME | ULTRA')], max_length=15),
        ),
        migrations.AlterField(
            model_name='building',
            name='trim',
            field=models.CharField(choices=[('Black', 'Black STANDARD | PRIME | ULTRA'), ('Charcoal', 'Charcoal STANDARD | PRIME | ULTRA'), ('Pewter', 'Pewter PRIME'), ('Gray', 'Gray STANDARD | PRIME | ULTRA'), ('Alamo', 'Alamo STANDARD | PRIME | ULTRA'), ('Brilliant', 'Brilliant STANDARD | PRIME | ULTRA'), ('Forest', 'Forest STANDARD | PRIME | ULTRA'), ('Hunter', 'Hunter STANDARD | PRIME | ULTRA'), ('Colony', 'Colony PRIME'), ('Crimson', 'Crimson PRIME | ULTRA'), ('Deep Red', 'Deep Red PRIME'), ('Rustic', 'Rustic STANDARD | PRIME | ULTRA'), ('Burgundy', 'Burgundy STANDARD | PRIME | ULTRA'), ('Gallery', 'Gallery PRIME | ULTRA'), ('Ocean', 'Ocean PRIME | ULTRA'), ('Ivory', 'Ivory PRIME'), ('Light Stone', 'Light Stone STANDARD | PRIME | ULTRA'), ('Desert', 'Desert PRIME'), ('Copper Metallic', 'Copper Metallic*† PRIME'), ('Galvalume', 'Galvalume STANDARD | PRIME | ULTRA'), ('Burnished Slate', 'Burnished Slate STANDARD | PRIME | ULTRA'), ('Brown', 'Brown STANDARD | PRIME | ULTRA'), ('Tan', 'Tan STANDARD | PRIME | ULTRA'), ('Taupe', 'Taupe STANDARD | PRIME | ULTRA')], max_length=20),
        ),
    ]
