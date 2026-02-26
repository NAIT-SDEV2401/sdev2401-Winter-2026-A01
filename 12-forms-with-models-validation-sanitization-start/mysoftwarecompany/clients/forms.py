from django import forms

# let's create a model form which will use the company model.
from .models import Company


class CompanyForm(forms.ModelForm):
    # we're going to setup the meta class
    # which will automatically generate the fields from the model.
    class Meta:
        model = Company
        fields = ['name', 'email', 'description']
        # we're not including created_at and updated_at because
        # they're automatically generated.

    # we're going to perform some cross field validation here.
    def clean(self):
        # we're going to call clean on the modelform itself.
        # calling clean on the parent class
        cleaned_data = super().clean()
        # list of forbiden words
        forbidden_words = ["scam", "fraud", "ponzi"]

        # let's get the name and description here
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        # loop through the words
        for forbidden_word in forbidden_words:
            # let's check here if it's in the forbidden words.
            if (forbidden_word in name.lower() or
                forbidden_word in description.lower()):
                    raise forms.ValidationError(
                        f"'{forbidden_word}' is not allowed to be used."
                    )
        # return it.
        return cleaned_data

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    # Custom validation for the name field
    # the <fieldname> method is used to add custom validation to a field.
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            # this will raise an validation error if the name is less than 2 characters long.
            raise forms.ValidationError("Name must be at least 2 characters long.")
        return name

    # Custom validation for the message field
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return message


