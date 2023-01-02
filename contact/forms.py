from django import forms
from .models import UserQuery, JobApplication


class ContactUsForm(forms.ModelForm):
    """
    Contact Us Form for submitting user queries to finechop
    """

    class Meta:
        model = UserQuery
        fields = (
            'name',
            'email',
            'comment',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email',
            'comment':
            'Enter your query/feedback here and we will be in touch..',
        }
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} '
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False


class JobApplicationForm(forms.ModelForm):
    """
    Job Application Us Form for submitting user queries to finechop
    """

    class Meta:
        model = JobApplication
        fields = (
            'first_name',
            'last_name',
            'email',
            'contact_number',
            'message',
            'resume',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'contact_number': 'Contact Number',
            'message': 'Message',
            'resume': 'Resume',
        }
        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} '
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
