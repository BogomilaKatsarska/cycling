from datetime import date

from django.core.exceptions import ValidationError


def validate_birthday_in_past(value):
    if date.today() < value:
        raise ValidationError('Birthday should be in the past')

