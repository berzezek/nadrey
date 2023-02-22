# Generated by Django 4.1.7 on 2023-02-19 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0005_alter_recipe_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='client',
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Оплачен')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitchen.client', verbose_name='Клиент')),
                ('order', models.ManyToManyField(to='kitchen.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
    ]
