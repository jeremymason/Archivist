from django.contrib import admin
from models import *

class ProgramParticipantInline(admin.TabularInline):
    model = ProgramParticipant
    extra = 1

class ProgramAdmin(admin.ModelAdmin):
    inlines = (ProgramParticipantInline,)
    list_display = ('title', 'description', 'genre', 'duration')
    search_fields = ('title', 'description')
    list_filter = ('title', 'genre')

admin.site.register(Program, ProgramAdmin)
admin.site.register(DigitalFile)
admin.site.register(DigitalFileLocation)
admin.site.register(SourceFormat)
admin.site.register(Source)
admin.site.register(Series)
admin.site.register(Rights)
admin.site.register(Genre)
admin.site.register(Subject)
admin.site.register(Person)
admin.site.register(Role)
