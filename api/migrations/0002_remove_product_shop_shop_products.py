# Generated by Django 4.1.3 on 2022-11-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='shop',
        ),
        migrations.AddField(
            model_name='shop',
            name='products',
            field=models.ManyToManyField(to='api.product'),
        ),
    ]
