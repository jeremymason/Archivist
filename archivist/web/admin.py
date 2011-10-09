from django.contrib import admin
from models import *

class DigitalFileParticipantInline(admin.TabularInline):
    model = DigitalFileParticipant
    extra = 1

class DigitalFileAdmin(admin.ModelAdmin):
    inlines = (DigitalFileParticipantInline,)


class SeriesParticipantInline(admin.TabularInline):
    model = SeriesParticipant
    extra = 1

class SeriesAdmin(admin.ModelAdmin):
    inlines = (SeriesParticipantInline,)


class SourceParticipantInline(admin.TabularInline):
    model = SourceParticipant
    extra = 1

class SourceAdmin(admin.ModelAdmin):
    inlines = (SourceParticipantInline,)


class ProgramParticipantInline(admin.TabularInline):
    model = ProgramParticipant
    extra = 1

class ProgramAdmin(admin.ModelAdmin):
    inlines = (ProgramParticipantInline,)
    list_display = ('title', 'description', 'duration')
    search_fields = ('title', 'description')
    list_filter = ('title',)


admin.site.register(Program, ProgramAdmin)
admin.site.register(DigitalFile, DigitalFileAdmin)
admin.site.register(DigitalFileLocation)
admin.site.register(SourceFormat)
admin.site.register(SourceLocation)
admin.site.register(Source, SourceAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Rights)
admin.site.register(Genre)
admin.site.register(Subject)
admin.site.register(Person)
admin.site.register(Role)
