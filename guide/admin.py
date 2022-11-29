from django.contrib import admin
from .models import SurfSpot, Danger, Photo, UserInformation, Comment

# Register your models here.
admin.site.register(SurfSpot)
admin.site.register(Danger)
admin.site.register(Photo)
admin.site.register(UserInformation)
admin.site.register(Comment)