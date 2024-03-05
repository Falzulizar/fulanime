from django.contrib import admin
from .models import Anime
from .models import Episode
from .models import Genre
from .models import RecommendedAnime
from .models import TrendingAnime
from .models import Comment
from .models import Movie

# Register your models here.
admin.site.register(Anime)
admin.site.register(Episode)
admin.site.register(Genre)
admin.site.register(RecommendedAnime)
admin.site.register(TrendingAnime)
admin.site.register(Comment)
admin.site.register(Movie)