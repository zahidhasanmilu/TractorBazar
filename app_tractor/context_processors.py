from .models import Tractor, TractorBrand
from django.shortcuts import render

def get_all_tractorBrand(request):
    tractorBrand = TractorBrand.objects.all().order_by('name')
    return {'all_tractorBrand': tractorBrand}






# def get_all_tags(request):
#     tags = Tag.objects.all().order_by('name')
#     return {'all_tags': tags}