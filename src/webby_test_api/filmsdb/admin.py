from django.contrib import admin
from filmsdb.models import Film, Actor


class FilmAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['title', 'year', 'format',]
    list_display_links = ['title',]
    list_filter = ['year', 'format',]
    search_fields = ['title',]


class ActorAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['name',]
    list_display_links = ['name',]
    search_fields = ['name',]


admin.site.register(Film, FilmAdmin)
admin.site.register(Actor, ActorAdmin)
