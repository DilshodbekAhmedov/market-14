# Generated by Django 4.2.1 on 2023-05-06 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Kategoriya nomi')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.category', verbose_name='Ota kategoriyasi')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Maxsulot nomi')),
                ('full_name', models.CharField(max_length=255, verbose_name="Maxsulotning to'liq nomi")),
                ('price', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Maxsulot narxi')),
                ('description', models.TextField(verbose_name="Maxsulot haqida ma'lumot")),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Maxsulot kategoriyasi')),
            ],
        ),
    ]
