from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('tractor/<slug:slug>/', views.tractor_details, name='tractor_details'),
    path('brand_all_tractors/<slug:slug>/', views.brand_all_tractors, name='brand_all_tractors'),
    path('search/', views.search_tractor, name='search_tractor'),

]