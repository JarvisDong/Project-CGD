from django import forms

class FileForm(forms.Form):
    name = forms.CharField(max_length=50)
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs = {"multiple": True}))
