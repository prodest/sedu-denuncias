from django.contrib import admin
from .models import *

class AlunoAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('nome','ra','cod_energia','escola')
    list_filter = (['escola'])
    search_fields = (['nome','ra','cod_energia'])

class AgenciaTransporteAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = (['nome'])
    list_filter = ('nome','sre')
    search_fields = (['nome'])

class EscolaAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = (['nome', 'municipio', 'cod_inep'])
    list_filter = (['municipio'])
    search_fields = (['nome', 'cod_inep'])

class MunicipioAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = (['nome', 'sre', 'cod_ibge'])
    list_filter = (['sre'])
    search_fields = (['nome', 'cod_ibge'])

class ReclamanteAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = (['nome', 'email'])
    search_fields = (['nome', 'email'])

class ResponsavelAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = (['usuario','sre'])
    list_filter = (['sre'])
    search_fields = (['usuario'])

class SreAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = (['name'])
    list_filter = ([])
    search_fields = (['name'])

class ComentarioInline(admin.StackedInline):
    model = Comentario
    extra = 0
    fields = ["responsavel", "texto"]

class ParecerFinalInline(admin.StackedInline):
    model = ParecerFinal
    extra = 0
    fields = ["responsavel", "texto"]
    

class ReclamacaoAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('aluno','protocolo', 'escola', 'setor', 'tipo', 'reclamante', 'status', 'rota')
    list_filter = ('agencia_transporte', 'status')
    search_fields = (['protocolo', 'aluno', 'rota'])
    inlines = [ComentarioInline, ParecerFinalInline]
    readonly_fields = ['protocolo', 'status']

    def escola(self, obj):
        return obj.aluno.escola
    
    def tipo(self, obj):
        return obj.tipo

    def setor(self, obj):
        return obj.tipo.setor

class TipoReclamacaoAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = (['nome'])
    search_fields = (['nome'])

class SetorAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = (['nome'])
    search_fields = (['nome'])

class TurnoAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = (['nome'])
    search_fields = (['nome'])

class RotaAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_filter = ('turno', 'escola')
    list_display = (['nome', 'turno', 'escola'])
    search_fields = (['nome', 'turno', 'escola'])


admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Escola, EscolaAdmin)
admin.site.register(AgenciaTransporte, AgenciaTransporteAdmin)
admin.site.register(SRE, SreAdmin)
admin.site.register(Reclamante, ReclamanteAdmin)
admin.site.register(Reclamacao, ReclamacaoAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Responsavel, ResponsavelAdmin)
admin.site.register(TipoReclamacao, TipoReclamacaoAdmin)
admin.site.register(Setor, SetorAdmin)
admin.site.register(Turno, TurnoAdmin)
admin.site.register(Rota, RotaAdmin)
