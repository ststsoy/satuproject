from django.contrib import admin


# Register your models here.
from homesatu.models import Homesatu,Insvid,Category
from newsself.models import Newsself,Addphoto


class HomesatuInline(admin.StackedInline):
    model = Insvid
    extra = 1


class HomesatuAdmin(admin.ModelAdmin):
    fields = ['title','content','photo','category_homesatu']
    inlines = [HomesatuInline]
    



admin.site.register(Homesatu,HomesatuAdmin)
admin.site.register(Category)
