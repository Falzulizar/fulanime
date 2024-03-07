# Generated by Django 5.0.3 on 2024-03-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0019_remove_comment_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='SwiperContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjudul', models.CharField(max_length=255)),
                ('judul', models.CharField(max_length=255)),
                ('deskripsi', models.TextField()),
                ('aksi', models.URLField()),
                ('image', models.ImageField(upload_to='swiper_images/')),
            ],
        ),
    ]
