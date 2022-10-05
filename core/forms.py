from django import forms
from .models import Form, Area, Experience


class FormForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ('logo', 'title', 'firstname', 'surname', 'address', 'programmer_title', 'summary' )

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['title', 'desc']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('work_date', 'company_name', 'desc', 'type_of', 'duration', 'role', 'technology', )
