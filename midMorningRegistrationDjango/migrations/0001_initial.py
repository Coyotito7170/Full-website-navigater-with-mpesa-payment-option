# Generated by Django 4.1.7 on 2023-03-07 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=30)),
                ('prod_quantity', models.CharField(max_length=30)),
                ('prod_price', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sup_name', models.CharField(max_length=30)),
                ('sup_email', models.CharField(max_length=30)),
                ('sup_phone', models.CharField(max_length=30)),
                ('sup_product', models.CharField(max_length=30)),
            ],
        ),
    ]
