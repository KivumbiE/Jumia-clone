# Generated by Django 4.2.2 on 2023-07-19 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0003_alter_productreviews_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchantuser',
            name='is_added_by_admin',
            field=models.BooleanField(default=False),
        ),
    ]