# Generated by Django 5.0.1 on 2024-02-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoshop', '0008_creditinfo_programm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditinfo',
            name='programm',
            field=models.ManyToManyField(blank=True, to='demoshop.creditprogram'),
        ),
        migrations.AlterField(
            model_name='creditprogram',
            name='lengh',
            field=models.IntegerField(blank=True, null=True, verbose_name='Срок кредита'),
        ),
        migrations.AlterField(
            model_name='creditprogram',
            name='overprice',
            field=models.IntegerField(blank=True, null=True, verbose_name='Переплата'),
        ),
        migrations.AlterField(
            model_name='creditprogram',
            name='vznos',
            field=models.IntegerField(blank=True, null=True, verbose_name='Первый взнос'),
        ),
        migrations.AlterField(
            model_name='promoblock',
            name='new_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Новая цена'),
        ),
        migrations.AlterField(
            model_name='promoblock',
            name='old_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Старая цена'),
        ),
    ]
