from django.shortcuts import render, HttpResponse
from app_tractor.models import Tractor


# Create your views here.
def home(request):
    tractors = Tractor.objects.all().order_by('created_at')
    context = {
        'tractors': tractors,
    }
    return render(request, 'app_tractor/home.html',context)
