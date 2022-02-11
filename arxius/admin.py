from django.utils.html import format_html
from django.contrib import admin
from .models import *

class CarpetaInLine(admin.TabularInline):
    model = Carpeta
    extra = 0
    exclude = ('nom', )
    readonly_fields = ['link','data_creacio', 'creador']
    list_display = ['link','data_creacio','creador']
    def link(self, obj):
        firm_url = '/admin/arxius/carpeta/'+str(obj.id)+'/change/'
        return format_html("<a href='{url}'>{nom}</a>", url=firm_url, nom=obj.nom)
class CarpetaAdmin(admin.ModelAdmin):
    exclude = ()
    inlines = [CarpetaInLine, ]
    def get_queryset(self, obj):
        return Carpeta.objects.filter(carpeta_pare = None)

# Register your models here.
admin.site.register(Carpeta , CarpetaAdmin)
admin.site.register(Arxiu)


