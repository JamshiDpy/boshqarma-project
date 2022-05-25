from django.contrib import admin
from .models import *


class RegionAdmin(admin.ModelAdmin):
    list_display = ("region_name","id",  "address", "admin")

class SchoolAdmin(admin.ModelAdmin):
    list_display = ("school_name", "region", "id", "type", "domain", "admin", "email")

class VideosAdmin(admin.ModelAdmin):
    list_display = ("school", "id")

class FotosAdmin(admin.ModelAdmin):
    list_display = ("school", "id")
class StaffAdmin(admin.ModelAdmin):
    list_display = ("full_name", "school", "id", "position")

class AchievementByTAdmin(admin.ModelAdmin):
    list_display = ("full_name", "id", "school")

class NewAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "school", "published_time")


admin.site.register(School, SchoolAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(New, NewAdmin)
admin.site.register(Event)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Excellent)
admin.site.register(Achivement)


admin.site.register(Videos, VideosAdmin)
admin.site.register(Fotos, FotosAdmin)
admin.site.register(AchievementByT, AchievementByTAdmin)
