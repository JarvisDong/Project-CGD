from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView

from django.utils import timezone
from .models import newdoc
from .forms import UploadFileForm, FileFieldForm

def upload_file(request):
    '''
    pass the file data from request into the form
    '''
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def upload_file_alter(request):
    '''
    save a file on a Model with a FileField using a ModelForm,
    file object will be saved to the location specified by the upload_to
    argument of the corresponding FileField when calling form.save()
    '''
    saved = False

    if request.method == "POST":
        form = FileFieldForm(request.POST, request.FILES)

        if form.is_valid():
            form = newdoc()
            form.save()
            saved = True
    else:
        form = FileFieldForm()
    return render(request, "upload.html", {"form": form})

def handle_uploaded_file(f):
    with open('file_name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class FileFieldView(FormView):
    '''
    override the post method of FormView subclass to
    handle multiple file uploads
    '''
    form_class = FileFieldForm
    template_name = "upload.html"
    success_url = '...' #undone:replace with proper URL

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist("file_field")
        if form.is_valid():
            #for f in files:
                 # Do something with each file, encrypt/watermark/rename to database/virus check
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
'''
class IndexView(ListView):
    model = newdoc
    template_name = "documents/index.html"

class PreView(DetailView):
    model = newdoc
    template_name='documents/detail.html'

class ResultView(DetailView):
    model = newdoc
    template_name = "documents/results.html"
'''

