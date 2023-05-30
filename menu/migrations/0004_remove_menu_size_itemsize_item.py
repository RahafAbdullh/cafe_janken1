# Generated by Django 4.2.1 on 2023-05-26 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_category_itemsize_remove_menu_price_remove_menu_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='size',
        ),
        migrations.AddField(
            model_name='itemsize',
            name='item',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='itemSize', to='menu.menu'),
            preserve_default=False,
        ),
    ]