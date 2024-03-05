"""
URL configuration for fulanime project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# myproject/urls.py

from django.contrib import admin
from django.urls import path
from anime import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('tes/', views.tes, name='tes'),
    path('anime/<int:anime_id>/', views.anime_detail, name='anime_detail'),
    path('anime-list/', views.anime_list, name='anime_list'),
    path('episode/<int:episode_id>/', views.episode_detail, name='episode_detail'),
    path('episode/<int:episode_id>/add_comment/', views.add_comment, name='add_comment'),
    path('ongoing-anime/', views.ongoing_anime, name='ongoing_anime'),
    path('add_comment/<int:episode_id>/', views.add_comment, name='add_comment'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)