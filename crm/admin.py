from django.contrib import admin
from .models import Lead, Funil, EtapaFunil

class LeadAdmin(admin.ModelAdmin):
  list_display = ('username', 'origem', 'email', 'data_captura')
  search_fields = ('username', 'email')

class FunilAdmin(admin.ModelAdmin):
  list_display = ('nome',)

class EtapaFunilAdmin(admin.ModelAdmin):
  list_display = ('funil', 'lead', 'nome', 'data_entrada', 'data_saida')
  list_filter = ('funil', 'nome')

admin.site.register(Lead, LeadAdmin)
admin.site.register(Funil, FunilAdmin)
admin.site.register(EtapaFunil, EtapaFunilAdmin)