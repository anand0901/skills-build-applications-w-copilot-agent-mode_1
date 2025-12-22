from django.urls import path, include

urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('activities/', include('apps.activities.urls')),
    path('teams/', include('apps.teams.urls')),
    path('leaderboard/', include('apps.leaderboard.urls')),
    path('workouts/', include('apps.workouts.urls')),
]