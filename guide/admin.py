from django.contrib import admin
from .models import SurfSpot, Danger, Photo, UserInformation, Comment, Season

# Register your models here.
admin.site.register(SurfSpot)
admin.site.register(Danger)
admin.site.register(Photo)
admin.site.register(UserInformation)
admin.site.register(Comment)
admin.site.register(Season)
