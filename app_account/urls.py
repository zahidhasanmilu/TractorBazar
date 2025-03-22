from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('contact_seller/', views.contact_seller, name='contact_seller'),

]