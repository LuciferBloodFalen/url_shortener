from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .models import UrlMapping
from rest_framework.generics import CreateAPIView
from .serializers import UrlMappingSerializer


class RedirectView(View):
    def get(self, request, short_code):
        url_obj = get_object_or_404(UrlMapping, short_code=short_code)

        url_obj.click_count += 1
        url_obj.save(update_fields=['click_count'])

        return redirect(url_obj.original_url)
    
class ShortenUrlAPIView(CreateAPIView):
    queryset = UrlMapping.objects.all()
    serializer_class = UrlMappingSerializer
    