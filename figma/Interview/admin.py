from django.contrib import admin
from.models import about,career
# Register your models here.
class aboutAdmin(admin.ModelAdmin):
    list_display = ('image_url','Description')
admin.site.register(about,aboutAdmin)

class careerAdmin(admin.ModelAdmin):
    list_display = ('Username','email','pdf')
admin.site.register(career,careerAdmin)