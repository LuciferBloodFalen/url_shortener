from django.urls import path
from .views import RedirectView, ShortenUrlAPIView

urlpatterns = [
    path('api/shorten/', ShortenUrlAPIView.as_view(), name="shorten-url"),
    path('<str:short_code>/', RedirectView.as_view(), name="redirect"),
]
