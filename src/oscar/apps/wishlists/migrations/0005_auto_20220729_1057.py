# Generated by Django 3.2.14 on 2022-07-29 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlists', '0004_auto_20220328_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='wishlistsharedemail',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
