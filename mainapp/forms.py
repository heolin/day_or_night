# -*- coding: utf-8 -*-
from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )

CHOICES = ((0.0, 'Night',), (1.0, 'Day',))
class ClassificationForm(forms.Form):
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, label="Choice")
