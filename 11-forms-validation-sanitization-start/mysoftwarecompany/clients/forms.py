# from django here we're going to import the forms module.
from django import forms

# this going to be what we use to validate our users data.
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

