from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.TeamListView.as_view(), name='team-list'),
    path('teams/<int:pk>/', views.TeamDetailView.as_view(), name='team-detail'),
    path('teams/create/', views.TeamCreateView.as_view(), name='team-create'),
    path('teams/<int:pk>/update/', views.TeamUpdateView.as_view(), name='team-update'),
    path('teams/<int:pk>/delete/', views.TeamDeleteView.as_view(), name='team-delete'),
]