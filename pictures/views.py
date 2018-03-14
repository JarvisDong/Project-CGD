from django.shortcuts import render
from .forms import PictureForm
from .models import Picture

def SavePicture(request):
    '''
    upload picture file, python photo library is required
    '''
    saved = False

    if request.method == "POST":
        #get the posted form
        MyPictureForm = PictureForm(request.POST,request.FILES)

        if MyPictureForm.is_valid():
            picture = Picture()
            picture.name = MyPictureForm.cleaned_data["name"]
            picture.picture = MyPictureForm.cleaned_data["picture"]
            picture.save()
            saved = True
    else:
        MyPictureForm = PictureForm()
    
    return render(request, "picture_saved.html", locals()) #locals: def Return a dictionary containing the current scope's local variables.
