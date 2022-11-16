from django.db import models


# Maps to a DB Table
class Cyclist(models.Model):
    MAX_FIRST_NAME = 30
    MAX_LAST_NAME = 30
    first_name = models.CharField(
        max_length=MAX_FIRST_NAME,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=MAX_LAST_NAME,
        null=False,
        blank=False,
    )
    # nationality = https://pypi.org/project/django-countries/
    photo = models.ImageField(
        null=True,
        blank=True,
    )
    birthday = models.DateField()
    # speciality = One Day Races, General Classification, Time Trail, Sprint, Climber
    # team
    description = models.TextField()
    strava_profile = models.URLField(
        null=True,
        blank=True,
    )
    facebook_profile = models.URLField(
        null=True,
        blank=True,
    )
    instagram_profile = models.URLField(
        null=True,
        blank=True,
    )
