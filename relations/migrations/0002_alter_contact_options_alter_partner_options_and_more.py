# Generated by Django 5.1.4 on 2024-12-16 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name': 'Партнёр', 'verbose_name_plural': 'Партнёры'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='partner',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='relations.contact', verbose_name='Контакты'),
        ),
    ]
