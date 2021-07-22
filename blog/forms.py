from django import forms
from .models import Essay

# creating a form
class EssayForm(forms.ModelForm):

    class Meta:
        model = Essay
        fields = ["title", "content"]

    


