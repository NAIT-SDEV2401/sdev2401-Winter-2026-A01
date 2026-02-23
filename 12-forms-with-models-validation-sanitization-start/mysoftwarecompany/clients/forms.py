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


