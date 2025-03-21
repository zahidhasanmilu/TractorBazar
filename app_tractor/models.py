import uuid
from datetime import date
from django.db import models
from django.utils.text import slugify
from app_account.models.managers import CustomUser
import os
###----------------------------------------------------------------


def tractor_brand_images_directory_path(instance, filename):
    return os.path.join('tractor_brand_images', instance.user.email, filename)
class TractorBrand(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='user_tractor_brands')
    name = models.CharField(max_length=100)
    slogan = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    logo = models.ImageField(upload_to=tractor_brand_images_directory_path) 
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)
    

    def save(self, *args, **kwargs):
        if not self.slug or self.slug.strip() == '':
            self.slug = slugify(self.name) + "-" + str(uuid.uuid4())[:8]
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Name: {self.name}  , Is active: {self.is_active}'
    
###----------------------------------------------------------------
    
class Tractor(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,related_name='user_tractors')
    name = models.CharField(max_length=255)  # ট্রাক্টরের নাম
    slug = models.SlugField(unique=True, blank=True)
    tractor_details = models.TextField(blank=True, null=True)  # ট্রাক্টরের বিস্তারিত বিবরণ
    brand = models.ForeignKey(TractorBrand, on_delete=models.SET_NULL, null=True, related_name='brand_tractors')
    model_year = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    condition = models.CharField(max_length=50, choices=[('new', 'New'), ('used', 'Used')]) 
    location = models.CharField(max_length=255)
    
    engine_power = models.IntegerField(help_text="Engine power in HP",blank=True, null=True)  # ইঞ্জিন পাওয়ার (HP)
    engine_type = models.CharField(max_length=50, choices=[('diesel', 'Diesel'), ('petrol', 'Petrol')], blank=True, null=True)  # ইঞ্জিন ধরন
    cylinder_count = models.IntegerField(blank=True, null=True)  # সিলিন্ডারের সংখ্যা
    fuel_capacity = models.IntegerField(help_text="Fuel capacity in liters", blank=True, null=True)  # জ্বালানি ধারণক্ষমতা
    mileage = models.FloatField(help_text="Mileage in KM per liter", blank=True, null=True)  # প্রতি লিটারে কিলোমিটার

    gearbox = models.CharField(max_length=50, blank=True, null=True)  # গিয়ার সংখ্যা
    brake_type = models.CharField(max_length=100, blank=True, null=True)  # ব্রেক ধরন
    steering_type = models.CharField(max_length=100)  # স্টিয়ারিং ধরন
    tyre_size = models.CharField(max_length=100,blank=True, null=True)  # টায়ারের মাপ
    hydraulics = models.IntegerField(help_text="Hydraulic lift capacity in KG", blank=True, null=True)  # হাইড্রোলিক লিফট ক্যাপাসিটি
    pto_power = models.IntegerField(help_text="PTO power in HP", blank=True, null=True)  # PTO HP
    drive_type = models.CharField(max_length=10, choices=[('2WD', '2WD'), ('4WD', '4WD')], blank=True, null=True)  # 2WD/4WD

    seller_name = models.CharField(max_length=255 , blank=True, null=True)  # বিক্রেতার নাম
    seller_contact = models.CharField(max_length=20, blank=True, null=True)  # বিক্রেতার মোবাইল নাম্বার
    seller_email = models.EmailField(blank=True, null=True )  # বিক্রেতার ইমেইল (যদি থাকে)

    registration_number = models.CharField(max_length=100, blank=True, null=True)  # রেজিস্ট্রেশন নম্বর (যদি থাকে)
    ownership_status = models.CharField(max_length=50, choices=[('first', 'First Owner'), ('second', 'Second Owner')],blank=True, null=True)  # মালিকানা অবস্থা
    insurance_status = models.BooleanField(default=False)  # ইনস্যুরেন্স আছে কি না

    is_active = models.BooleanField(default=False)  # ফিচারড ট্রাক্টর কিনা
    created_at = models.DateTimeField(auto_now_add=True)  # পোস্টের সময়
    updated_at = models.DateTimeField(auto_now=True)  # আপডেটের সময়

    
    def save(self, *args, **kwargs):
        if not self.slug or self.slug.strip() == '':
            self.slug = slugify(self.name) + "-" + str(uuid.uuid4())[:8]
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.name} - {self.brand.name} ({self.model_year})"


###----------------------------------------------------------------

def tractor_images_directory_path(instance, filename):
    return os.path.join('tractor_images', instance.user.email, filename)

class TractorImage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True , related_name='user_images')
    tractor = models.ForeignKey(Tractor, on_delete=models.CASCADE, related_name="tractor_images")  # ট্রাক্টরের সাথে সম্পর্ক
    image = models.ImageField(upload_to=tractor_images_directory_path)  # ইমেজ আপলোড করার ফিল্ড
    created_at = models.DateTimeField(auto_now_add=True)  # পোস্টের সময়
    updated_at = models.DateTimeField(auto_now=True)  # আপডেটের সময়

    def __str__(self):
        return f"Image for {self.tractor.name}"
    
###----------------------------------------------------------------
def tractor_videos_directory_path(instance, filename):
    return os.path.join('tractor_videos', instance.user.email, filename)

class TractorVideo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,  related_name='user_videos')
    tractor = models.ForeignKey(Tractor, on_delete=models.CASCADE, related_name="tractor_videos")  # ট্রাক্টরের সাথে সম্পর্ক
    video = models.FileField(upload_to=tractor_videos_directory_path)  # video আপলোড করার ফিল্ড
    created_at = models.DateTimeField(auto_now_add=True)  # পোস্টের সময়
    updated_at = models.DateTimeField(auto_now=True)