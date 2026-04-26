from django.contrib import admin
from .models import Movie, Genre


@admin.register(Genre)  # NUEVO
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )

    search_fields = (
        "name",
    )


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "release_date",
        "duration",
    )

    search_fields = (
        "title",
    )

    filter_horizontal = (
        "genres",
    )