from django import forms


class CyclistForm(forms.Form):
    your_name = forms.CharField(
        max_length=30,
        label='Name',
        help_text="Enter your name",
    )
    age = forms.IntegerField(
        required=False,
        initial=0,
    )
