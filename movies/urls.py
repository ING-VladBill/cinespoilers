from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movies.views import (
    MovieViewSet,
    GenreViewSet
)

router = DefaultRouter()

router.register(
    r'movies',
    MovieViewSet
)

router.register(  # NUEVO
    r'genres',
    GenreViewSet
)

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),

    path(
        'api/',
        include(router.urls)
    ),
]