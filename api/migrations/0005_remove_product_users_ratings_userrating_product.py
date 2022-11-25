# Generated by Django 4.1.3 on 2022-11-25 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_product_shop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='users_ratings',
        ),
        migrations.AddField(
            model_name='userrating',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.product'),
        ),
    ]
