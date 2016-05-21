from django.contrib import admin

# Register your models here.
from portfolio.models import Images, Albums




class AdminImage(admin.ModelAdmin):
    readonly_fields = ('img',)
    fields = ('name','img','img_src','img_link','img_description')
    list_display = ('img','img_description')


admin.site.register(Images,AdminImage)

admin.site.register(Albums)

