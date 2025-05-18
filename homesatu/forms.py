__author__ = 'admin'
from django.forms import ModelForm
from homesatu.models import Invid
class InvidForm(ModelForm):
    class Meta():
        model = Invid
        fields =['title','content','video']
