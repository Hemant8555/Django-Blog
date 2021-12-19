from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="userhome"),
    path('funding/', views.funding, name="fundings"),
    path('leaderboard/', views.leaderboard, name="leaderboard"),
    path('team/', views.team, name="team"),
    path('profile/<str:username>', views.profile, name="user_profile"),
    path('user/', include('users.urls')),
    path('home/', include('tweets.urls')),
]
