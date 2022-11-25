from django.db import models
from django_countries.fields import CountryField
from cycling.teams.models import Team


# Maps to a DB Table
class Cyclist(models.Model):
    class Meta:
        ordering = ('first_name', 'last_name')

    ONE_DAY_RACES_SPECIALTY = 'One Day Races'
    GC_SPECIALTY = 'General Classification'
    TT_SPECIALTY = 'Time Trail'
    S_SPECIALTY = 'Sprint'
    C_SPECIALTY = 'Climber'

    SPECIALTIES = (
        (ONE_DAY_RACES_SPECIALTY, ONE_DAY_RACES_SPECIALTY),
        (GC_SPECIALTY, GC_SPECIALTY),
        (TT_SPECIALTY, TT_SPECIALTY),
        (S_SPECIALTY, S_SPECIALTY),
        (C_SPECIALTY, C_SPECIALTY),
    )

    MAX_FIRST_NAME = 30
    MAX_LAST_NAME = 30
    MAX_SPECIALTY_LEN = 30

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
    country = CountryField()
    photo = models.ImageField(
        null=True,
        blank=True,
    )
    birthday = models.DateField()
    open_for_new_opportunities = models.BooleanField()
    speciality = models.CharField(
        max_length=MAX_SPECIALTY_LEN,
        choices=SPECIALTIES,
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
    )
    description = models.TextField()
    mail = models.EmailField(
        verbose_name='e-mail',
        null=True,
        blank=True,
        unique=True,
    )
    strava_profile = models.URLField(
        null=True,
        blank=True,
        unique=True,
    )
    facebook_profile = models.URLField(
        null=True,
        blank=True,
        unique=True,
    )
    instagram_profile = models.URLField(
        null=True,
        blank=True,
        unique=True,
    )
    slug = models.SlugField(
        unique=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'ID: {self.pk} - Name: {self.full_name}'

    # visits
