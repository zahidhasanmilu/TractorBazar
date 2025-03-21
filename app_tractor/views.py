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


#-------------------search---------------------------------------------
def search_tractor(request):
    search_item = request.GET.get('search', '').strip()  # ইউজার ইনপুট নিলাম
    
    tractors = Tractor.objects.none()  # ডিফল্টভাবে কোনো ট্রাক্টর না পাঠানো
    
    if search_item:  # সার্চ টার্ম থাকলে ফিল্টার করবো
        tractors = Tractor.objects.filter(
            Q(name__icontains=search_item) |     # নাম দিয়ে সার্চ
            Q(brand__name__icontains=search_item) |  # ব্র্যান্ড দিয়ে সার্চ
            Q(model_year__icontains=search_item)  # মডেল ইয়ার দিয়ে সার্চ
        ).order_by('is_active')

    context = {
        'tractors': tractors,
        'search_item': search_item
    }
    return render(request, 'app_tractor/search_results.html', context)
