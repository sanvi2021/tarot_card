
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .models import *




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name = 'index.html'),
    path('services/',views.services,name ="services.html"),
    path('contact/',views.contact, name = "contact.html"),
    path('about/',views.about,name ='about.html'),
    # path('download/',views.download,name ='download.html'),

]
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)
