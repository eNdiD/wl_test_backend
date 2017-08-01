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
    list_display = ['first_name', 'last_name']
    list_display_links = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']


admin.site.register(Film, FilmAdmin)
admin.site.register(Actor, ActorAdmin)
