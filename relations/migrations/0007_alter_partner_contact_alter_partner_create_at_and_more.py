# Generated by Django 5.1.4 on 2024-12-20 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0006_alter_partner_contact_alter_partner_create_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='relations.contact', verbose_name='Контакты'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='debt',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Задолженность'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='products',
            field=models.ManyToManyField(to='relations.product', verbose_name='Продукты'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='relations.partner', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='type_organization',
            field=models.IntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'ИП')], verbose_name='Тип организации'),
        ),
    ]
