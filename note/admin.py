from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at',
                    'created_by', 'priority')


admin.site.register(Note, NoteAdmin)
