# Generated by Django 5.0.3 on 2024-03-07 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0020_swipercontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swipercontent',
            name='aksi',
            field=models.TextField(),
        ),
    ]
