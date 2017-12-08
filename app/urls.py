from django.conf.urls import url

from app.views import CustomObtainAuthToken

urlpatterns = [
    url(r'^authenticate/', CustomObtainAuthToken.as_view()),
]
