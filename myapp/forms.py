from django import forms

class UserEForm(forms.Form):
    username   = forms.CharField(max_length=150)
    email      = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=False)
    last_name  = forms.CharField(max_length=30, required=False)
    bio        = forms.CharField(widget=forms.Textarea, required=False)
