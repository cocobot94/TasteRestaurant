# Generated by Django 5.0.1 on 2024-01-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_image_alter_products_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default='core/templates/core/menu_1.jpg', upload_to='products/'),
        ),
    ]
