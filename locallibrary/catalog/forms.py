from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from . import models


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        #we get our data using self.cleaned_data['renewal_date'] and that we return this data whether or not we change it at the end of the function
        data = self.cleaned_data['renewal_date']
        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        
        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
        
        # Remember to always return the cleaned data.
        return data

class AuthorForm(forms.ModelForm):
    class Meta:
        model=models.Author
        fields=['first_name','last_name','date_of_birth','date_of_death']

class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['title','summary','isbn','genre','image']        


class UserProfileForm(forms.ModelForm):
    class Meta:
        model=models.UserProfile
        fields=['phone','image']                