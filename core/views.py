from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib import messages
from .models import UrlMapping
from .forms import UrlShortenForm
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
    

def index(request):
    """Main page with URL shortening functionality"""
    form = UrlShortenForm()
    shortened_url = None
    recent_urls = []
    
    if request.method == 'POST':
        if 'clear_history' in request.POST:
            request.session['recent_urls'] = []
            messages.success(request, 'History cleared successfully!')
            return redirect('index')
        else:
            form = UrlShortenForm(request.POST)
            if form.is_valid():
                original_url = form.cleaned_data['original_url']
                url_mapping = UrlMapping.objects.create(original_url=original_url)
                
                shortened_url = {
                    'short_url': request.build_absolute_uri(f'/{url_mapping.short_code}/'),
                    'original_url': url_mapping.original_url,
                    'short_code': url_mapping.short_code,
                    'created_at': url_mapping.created_at
                }
                
                if 'recent_urls' not in request.session:
                    request.session['recent_urls'] = []
                
                request.session['recent_urls'].insert(0, {
                    'short_url': shortened_url['short_url'],
                    'original_url': url_mapping.original_url,
                    'short_code': url_mapping.short_code,
                    'created_at': url_mapping.created_at.isoformat()
                })
                
                request.session['recent_urls'] = request.session['recent_urls'][:10]
                request.session.modified = True
                
                messages.success(request, 'URL shortened successfully!')
    
    recent_urls = request.session.get('recent_urls', [])
    
    context = {
        'form': form,
        'shortened_url': shortened_url,
        'recent_urls': recent_urls
    }
    
    return render(request, 'index.html', context)
    