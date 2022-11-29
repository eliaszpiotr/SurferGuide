from django.contrib import admin
from .models import SurfSpot, Danger, Photo

# Register your models here.
admin.site.register(SurfSpot)
admin.site.register(Danger)
admin.site.register(Photo)