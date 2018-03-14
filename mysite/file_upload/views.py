from django.shortcuts import render
from .models import File
from .forms import FileForm
 
# Create your views here.
def SaveFile(request):
    saved = False
    
    if request.method == "POST":
        #get the posted form
        MyFileForm = FileForm(request.POST, request.FILES)
        if MyFileForm.is_valid():
            f = File()
            f.name = MyFileForm.cleaned_data["name"]
            f.File = MyFileForm.cleaned_data["file"]
            f.save()
            saved = True
    else:
        MyFileForm = FileForm()
    
    return render(request, "file_saved.html", {"form": MyFileForm})
            

