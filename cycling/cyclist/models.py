from django.db import models


# Maps to a DB Table
class Cyclist(models.Model):
    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    birthday = models.DateField()
    description = models.TextField()
