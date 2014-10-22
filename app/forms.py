from django import forms
from app.models import Sufficiency
from crispy_forms.helper import FormHelper
 
class SufficiencyForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
 
    class Meta:
        model = Sufficiency
