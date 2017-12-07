from app.models import Deck, Player, Card
from rest_framework import viewsets
from app.serializers import DeckSerializer, PlayerSerializer

class DeckViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows deck to be viewed or edited.
    """
    queryset = Deck.objects.all().order_by('-date_joined')
    serializer_class = DeckSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Player to be viewed or edited.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
