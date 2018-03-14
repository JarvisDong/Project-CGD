from django import forms
'''
data from the form would be accessible as request.FILES["file"]
request.FILE will only contain data if the request method was POST
and the <form> that posted the request has the attribute enctype="multipart/form-data"
'''
class UploadFileForm(forms.Form):
    '''
    a simple form containing a FileField.
    '''
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class FileFieldForm(forms.Form):
    '''
    upload multiple files using one form field.
    '''
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs = {"multiple": True}))




















'''
Testing for multipart forms

If you’re writing reusable views or templates,
you may not know ahead of time whether your form is a multipart form or not.
The is_multipart() method tells you whether the form requires multipart encoding
for submission:

Form.is_multipart()
>>> f = ContactFormWithMugshot()
>>> f.is_multipart()
True

template sample

{% if form.is_multipart %}
    <form enctype="multipart/form-data" method="post" action="/foo/">
{% else %}
    <form method="post" action="/foo/">
{% endif %}
{{ form }}
</form>
'''