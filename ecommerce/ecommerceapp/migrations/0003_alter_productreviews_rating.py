# Generated by Django 4.2.2 on 2023-07-10 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0002_categories_customerorders_customeruser_merchantuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreviews',
            name='rating',
            field=models.CharField(default='5', max_length=255),
        ),
    ]