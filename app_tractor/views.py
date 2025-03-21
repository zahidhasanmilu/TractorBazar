from django.shortcuts import get_object_or_404, render, HttpResponse
from app_tractor.models import Tractor, TractorBrand
from django.db.models import Q

# Create your views here.
##-------------------------home---------------------------------------
def home(request):
    tractors = Tractor.objects.all().order_by('created_at')
    context = {
        'tractors': tractors,
    }
    return render(request, 'app_tractor/home.html',context)



##-------------------------tractor_details---------------------------------------
def tractor_details(request, slug):
    tractor = get_object_or_404(Tractor, slug=slug)
    context = {
        'tractor': tractor,
    }
    return render(request, 'app_tractor/tractor_details.html', context)


##-------------------------brand_all_tractors---------------------------------------
def brand_all_tractors(request, slug):
    brand_tractor = get_object_or_404(TractorBrand, slug=slug)
    tractors = brand_tractor.brand_tractors.all().order_by('created_at')  # এখন কাজ করবে

    context = {
        'tractors': tractors,
        'brand_tractor': brand_tractor,
    }
    return render(request, 'app_tractor/brand_tractors.html', context)

