from django import forms

class PictureForm(forms.Form):
    '''
    upload image files using one form field.
    '''
    name = forms.CharField(max_length=100)
    picture = forms.ImageField()
