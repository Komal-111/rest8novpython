from django import forms
from .models import blog

class blogForm(forms.ModelForm):
    class Meta:
        model=blog
        fields='__all__'
    

class updateForm(forms.ModelForm):
    class Meta:
        model=blog
        fields=['created','title','content','updated']
