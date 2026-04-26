from django.db import models


class Genre(models.Model):  # NUEVO
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(
        max_length=255
    )

    description = models.TextField()

    release_date = models.DateField()

    duration = models.PositiveIntegerField(
        help_text="Duration in minutes"
    )

    genres = models.ManyToManyField(  # NUEVO
        Genre,
        related_name="movies",
        blank=True
    )

    def __str__(self):
        return self.title
    
