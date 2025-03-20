from .models import TractorBrand

def get_all_tractorBrand(request):
    tractorBrand = TractorBrand.objects.all().order_by('name')
    return {'all_tractorBrand': tractorBrand}

# def get_all_tags(request):
#     tags = Tag.objects.all().order_by('name')
#     return {'all_tags': tags}