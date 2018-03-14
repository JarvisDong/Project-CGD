# URLconf: map the index view in view.py to a URL
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name = 'documents'
urlpatterns = []