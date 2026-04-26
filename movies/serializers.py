from rest_framework import serializers
from .models import Movie, Genre, ShowTime


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