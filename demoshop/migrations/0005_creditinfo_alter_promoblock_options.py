# Generated by Django 5.0.1 on 2024-01-28 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoshop', '0004_promoblock_delete_menubutton'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_text', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('my_field', models.CharField(choices=[('value1', 'Value 1'), ('value2', 'Value 2'), ('value3', 'Value 3')], max_length=10)),
            ],
        ),
        migrations.AlterModelOptions(
            name='promoblock',
            options={'verbose_name': 'Акция', 'verbose_name_plural': 'Акции'},
        ),
    ]