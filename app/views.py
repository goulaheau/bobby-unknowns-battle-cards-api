from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from app.models import Deck, User, Card
from app.serializers import DeckSerializer, UserSerializer, CardSerializer


class DeckViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Deck to be viewed or edited.
    """
    queryset = Deck.objects.all().order_by('-date_joined')
    serializer_class = DeckSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows User to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Card to be viewed or edited.
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args,
                                                           **kwargs)

        token = Token.objects.get(key=response.data['token'])

        return Response({'token': token.key,
                         'user': UserSerializer(token.user).data})
