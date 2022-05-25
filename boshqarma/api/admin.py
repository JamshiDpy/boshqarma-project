from django.contrib import admin
from .models import *

class BoshqarmaAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "id", "domain", "email", )

class RegionAdmin(admin.ModelAdmin):
    list_display = ("name", "full_name", "domain", "email", )
#    list_filter = ("name", "domain")
class HujjatlarAdmin(admin.ModelAdmin):
    list_display = ("title", "link", "type", )
#    list_filter = ("title", "link", "type",)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ("name", "id",)

class RahbariyatAdmin(admin.ModelAdmin):
    list_display = ("full_name","id", "spec", "phone", "email",)

class MurojaatAdmin(admin.ModelAdmin):
    list_display = ("name", "id","phone", "text",)

class NewsAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "date_added")


admin.site.register(Boshqarma, BoshqarmaAdmin)
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Rahbariyat, RahbariyatAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Murojaat, MurojaatAdmin)
admin.site.register(Verification)
admin.site.register(Events)
admin.site.register(Hujjatlar, HujjatlarAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Foto_lavhalar)
admin.site.register(Presentations)
admin.site.register(Projects)
