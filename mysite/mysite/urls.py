"""URL Configuration

Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include #point the root URLconf at the polls.urls module
from django.conf import settings #for MEDIA_URL

urlpatterns = [
    #always use include() when include other URL patterns.
    url(r'^polls/', include('polls.urls')), 	
    url(r'^documents/',include('documents.urls')),
    url(r'^pictures/',include("pictures.urls")),
    url(r'^admin/', admin.site.urls), #admin.site.urls is the only exception. 
]

if settings.DEBUG:
    urlpatterns += urlpatterns[
        url(
        r"^media/(?P<path>.*)$", 
        "django.views.static.serve", 
        {"document_root": settings.MEDIA_ROOT,}
        )
    ]