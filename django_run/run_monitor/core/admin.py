from django.contrib import admin

# Register your models here.
from .models import Run
from .models import RunSteps

# personalizar a tela de admin com a exibicao e os campos de busca
class RunAdmin (admin.ModelAdmin):
    list_display = ['id_run', 'run_date' ]
    search_fields = ['id_run']

admin.site.register(Run, RunAdmin)
admin.site.register(RunSteps)