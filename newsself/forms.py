from django import forms 
from newsself.models import*
class AddphotoForm(forms.ModelForm):
    class Meta():
        model = Addphoto
        fields ='__all__'