# Generated by Django 4.2.7 on 2023-11-30 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0004_alter_anime_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='status',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('Complete', 'Complete')], default='Ongoing', max_length=10),
        ),
    ]
