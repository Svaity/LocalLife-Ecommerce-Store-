# Generated by Django 3.0.3 on 2020-04-28 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('user', '0003_auto_20200424_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ebooks',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]