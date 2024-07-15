from django.contrib import admin
from .models import PersonalInfo, InfoReview, Plateform, InfoCertificate

# Register your models here.

class InfoReviewInline(admin.TabularInline):
    model = InfoReview
    extra = 2

class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_of_chai', 'date_added')
    inlines = [InfoReviewInline]

class PlateformAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('infos',)

class InfoCertificateAdmin(admin.ModelAdmin):
    list_display = ('info', 'certifiacte_number')

admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(Plateform, PlateformAdmin)
admin.site.register(InfoCertificate, InfoCertificateAdmin)