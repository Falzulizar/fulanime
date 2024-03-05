from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Anime, Episode, Comment, RecommendedAnime, TrendingAnime, Genre, Movie

def index(request):
    anime_list = Anime.objects.all()
    movie_list = Movie.objects.all()
    recommended_animes = RecommendedAnime.objects.all()
    trending_animes = TrendingAnime.objects.all()

    context = {
        'anime_list': anime_list,
        'recommended_animes': recommended_animes,
        'trending_animes': trending_animes,
        'movie_list' : movie_list
    }

    return render(request, 'index.html', context)

def anime_detail(request, anime_id):
    anime = get_object_or_404(Anime, pk=anime_id)
    return render(request, 'anime_detail.html', {'anime': anime})

def episode_detail(request, episode_id):
    episode = get_object_or_404(Episode, pk=episode_id)
    comments = Comment.objects.filter(episode=episode)
    trending_animes = TrendingAnime.objects.all()

    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        comment_text = request.POST.get('comment_text')

        print("User Name:", user_name)
        print("Comment Text:", comment_text)

        Comment.objects.create(user_name=user_name, comment_text=comment_text, episode=episode,)
        messages.success(request, 'Comment added successfully.')

        return redirect('episode_detail', episode_id=episode.id)

    return render(request, 'episode_detail.html', {'episode': episode, 'comments': comments, 'trending_animes': trending_animes})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    return render(request, 'movie_detail.html', {'movie': movie})

def movie_list(request):
    genres = Genre.objects.all()
    selected_genre = request.GET.get('genre')
    search_query = request.GET.get('q')

    if selected_genre:
        movie_list = Movie.objects.filter(genres__name=selected_genre)
    elif search_query:  # Periksa apakah ada parameter pencarian
        movie_list = Movie.objects.filter(title__icontains=search_query)
    else:
        movie_list = Movie.objects.all()

    context = {'movie_list': movie_list, 'genres': genres, 'selected_genre': selected_genre, 'query': search_query}  # Tambahkan 'query' ke context
    return render(request, 'movie_list.html', context)

def anime_list(request):
    genres = Genre.objects.all()
    selected_genre = request.GET.get('genre')
    search_query = request.GET.get('q')  # Tambahkan ini

    if selected_genre:
        anime_list = Anime.objects.filter(genres__name=selected_genre)
    elif search_query:  # Periksa apakah ada parameter pencarian
        anime_list = Anime.objects.filter(title__icontains=search_query)
    else:
        anime_list = Anime.objects.all()

    context = {'anime_list': anime_list, 'genres': genres, 'selected_genre': selected_genre, 'query': search_query}  # Tambahkan 'query' ke context
    return render(request, 'anime_list.html', context)

def ongoing_anime(request):
    ongoing_anime_list = Anime.objects.filter(status=Anime.ONGOING)
    return render(request, 'ongoing_anime.html', {'ongoing_anime_list': ongoing_anime_list})

def add_comment(request, episode_id):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        comment_text = request.POST['comment_text']
        episode = get_object_or_404(Episode, id=episode_id)

        # Simpan komentar ke database
        Comment.objects.create(user_name=user_name, comment_text=comment_text, episode=episode)

    return redirect('episode_detail', episode_id=episode_id)

