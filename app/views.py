from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from app.models import Deck, Player, Card
from app.serializers import DeckSerializer, PlayerSerializer, CardSerializer


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


class CardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Player to be viewed or edited.
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args,
                                                           **kwargs)

        token = Token.objects.get(key=response.data['token'])

        player = Player.objects.get(user=token.user_id)

        return Response({'token': token.key,
                         'player': PlayerSerializer(player).data})
