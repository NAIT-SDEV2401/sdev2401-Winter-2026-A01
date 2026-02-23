# from django here we're going to import the forms module.
from django import forms

# docs for form fields here: https://docs.djangoproject.com/en/5.2/ref/forms/fields

# this going to be what we use to validate our users data.
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    # some validation to make sure that the name is greater
    # than two characters.
    def clean_name(self):
        # get the name from the cleaned_data
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError(
                "name must be greater than 2 characters."
            )
        # return the value if it's valid.
        return name

    # message needs to be more than ten characters
    # message needs to be more than two words.
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError(
                "the message needs to be more than 10 characters"
            )

        words = message.split(' ')
        word_count = len(words)
        if word_count <= 2:
            raise forms.ValidationError(
                "needs to be more than two words."
            )

        return message