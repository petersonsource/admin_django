from xml.dom import NO_MODIFICATION_ALLOWED_ERR

from django.contrib import admin
from .models import Usuario, Loja, Perfil, UsuarioPerfil

# Register your models here.

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'loja')
    list_filter = ('loja',)
    search_fields = ('nome', 'codigo')
    ordering = ('nome',)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id','nome', 'email')
    list_editable = ('email',)
    link_display_links = ('nome',)
    search_fields = ('nome', 'email')
    ordering = ('id',)

@admin.register(Loja)
class LojaAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'appkey', 'apptoken')
    link_display_links = ('account',)
    list_filter = ('id','account',)
    search_fields = ('account',)
    ordering = ('id',)

class UsuarioPerfilInline(admin.TabularInline):
    model = UsuarioPerfil
    extra = 1
    autocomplete_fields = ('usuario',)

@admin.register(UsuarioPerfil)
class UsuarioPerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'perfil', 'get_loja')
    list_filter = ('perfil__loja',)

    def get_loja(self, obj):
        return obj.perfil.loja.account
    get_loja.short_description = 'Loja'
    get_loja.admin_order_field = 'perfil__loja__account'