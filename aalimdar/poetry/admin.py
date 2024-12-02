from django.contrib import admin
from .models import Poetry

class PoetryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    fields = ('title', 'author', 'lines')  

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'lines':
            kwargs['widget'] = admin.widgets.AdminTextareaWidget(attrs={'rows': 10, 'cols': 60})  
        return super().formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Poetry, PoetryAdmin)
