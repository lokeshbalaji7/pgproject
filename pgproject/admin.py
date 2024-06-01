from django.contrib import admin
from .models import PG, PGImage, Registrations

# Register your models here.


@admin.register(PG)
class PGAdmin(admin.ModelAdmin):
    list_display = ['PG_Code', 'Name', 'PG_Name', 'Address', 'Phn_no', 'rating', 'description']

@admin.register(PGImage)
class PGImageAdmin(admin.ModelAdmin):
    list_display = ['PG_code', 'Sharing', 'price', 'vacancies', 'image']


@admin.register(Registrations)
class Registrations(admin.ModelAdmin):
    list_display = ['Registration_id','Full_name','Email','Mobile_number','sharing_person','price_person']