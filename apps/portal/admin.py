from django.contrib import admin
from .models import EquipeMembro, Inicial, QuemSomos, Curso, SecaoAprovados, Aprovados, Parceiros, Contatos, SecaoEquipe

# Register your models here.
class InicialAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'texto', 'data']

class QuemSomosAdmin(admin.ModelAdmin):
    list_display = ['texto', 'data']

class EquipeAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'subtitulo', 'data']

class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data']

class SecaoAprovadosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'subtitulo', 'data']

class AprovadosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'instituicao', 'data']

class ParceirosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'imagem', 'data']

class ContatosAdmin(admin.ModelAdmin):
    list_display = ['instagram', 'facebook', 'data']

admin.site.register(Inicial, InicialAdmin)
admin.site.register(QuemSomos, QuemSomosAdmin)
admin.site.register(SecaoEquipe, EquipeAdmin)
admin.site.register(EquipeMembro)
admin.site.register(Curso, CursoAdmin)
admin.site.register(SecaoAprovados, SecaoAprovadosAdmin)
admin.site.register(Aprovados, AprovadosAdmin)
admin.site.register(Parceiros, ParceirosAdmin)
admin.site.register(Contatos, ContatosAdmin)