import imp
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.books, name='books'),
    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete'),
    path('f', views.f, name='f'),
    
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)