from rest_framework import viewsets
from .models import Leaderboard
from .serializers import LeaderboardSerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

    def get_queryset(self):
        # Optionally filter the queryset based on request parameters
        queryset = super().get_queryset()
        # Add any filtering logic here if needed
        return queryset