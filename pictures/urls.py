from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name = 'pictures'

urlpatterns =[
    url(r'^$/',TemplateView.as_view(template_name = 'picture.html')),
    url(r'^$/', views.SavePicture, name = 'saved')
]