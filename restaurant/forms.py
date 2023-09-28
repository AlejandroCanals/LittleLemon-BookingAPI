from .models import Booking
from django import forms

class BookingForm(forms.ModelForm):

#This class is used to provide meta information about the form, such as the model it is linked to and the fields that should be included in the form.  
    class Meta:
        model = Booking
        fields = "__all__"
        