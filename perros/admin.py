from django.contrib import admin

from perros.models import Perro,Comentario

class PerroAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Comentario)
admin.site.register(Perro, PerroAdmin)
