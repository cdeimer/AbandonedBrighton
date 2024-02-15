from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Location

# Create your views here.
def index(request):
    featured_pages = featured_pages = Location.objects.order_by('-last_updated')[:8]  # Get recent
    context = {
        'featured_pages': featured_pages,
        'placeholder_counter': placeholder_page_helper(featured_pages)
    }
    return render(request, 'pages/home_page.html', context)

def location_detail(request, location_id):
    try:
        location = Location.objects.get(pk=location_id)
        context = {'location': location}
    except:
        raise Http404("Location does not exist.")
    return render(request, "pages/location_detail.html", context)

def placeholder_page_helper(featured_pages_list: list):
    return [0 for i in range(8 - len(featured_pages_list))]