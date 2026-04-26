from rest_framework import serializers
from .models import Movie, Genre, ShowTime
from .models import Sala


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = [
            "id",
            "name"
        ]


class MovieSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "release_date",
            "duration",
            "genres"
        ]


class ShowTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTime
        fields = '__all__'

class SalaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sala
        fields = [
            "id",
            "nombre",
            "capacidad"
        ]