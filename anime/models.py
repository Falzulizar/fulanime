from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    cover_image = models.ImageField(upload_to='movie_covers/', null=True, blank=True)
    video_url = models.URLField()

    def __str__(self):
        return self.title


class Anime(models.Model):
    ONGOING = 'Ongoing'
    COMPLETE = 'Complete'
    
    STATUS_CHOICES = [
        (ONGOING, 'Ongoing'),
        (COMPLETE, 'Complete'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre)
    cover_image = models.ImageField(upload_to='anime_covers/', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ONGOING)

    def __str__(self):
        return self.title

    def episode_count(self):
        return self.episode_set.count()

class Episode(models.Model):
    title = models.CharField(max_length=255)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    episode_number = models.IntegerField()
    video_url = models.URLField()

    def __str__(self):
        return f"{self.anime.title} - Episode {self.episode_number}"

class RecommendedAnime(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self):
        return f"Recommended: {self.anime.title}"

class TrendingAnime(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self):
        return f"Trending: {self.anime.title}"

class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    comment_text = models.TextField()
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} on {self.episode.anime.title} - Episode {self.episode.episode_number}"

class SwiperContent(models.Model):
    subjudul = models.CharField(max_length=255)
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    aksi = models.CharField(max_length=255)
    image = models.ImageField(upload_to='swiper_images/')

    def __str__(self):
        return self.judul