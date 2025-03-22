from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import CustomUser




# #-------------------contact_seller---------------------------------------------

def contact_seller(request):

    seller = get_object_or_404(CustomUser, email="minions.milu889@gmail.com")
    context = {
        'seller': seller,
    }
    return render(request, 'app_account/contact.html', context)


