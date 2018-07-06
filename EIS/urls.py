from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include

from . import views

urlpatterns = [
    path('favicon.ico',                  RedirectView.as_view(url='/static/favicon.ico', permanent=True)),

    path('media/pdf/<str:filename>',     views.pdf_download),
    path('media/file/<str:filename>',    views.file_download),

    path('admin/logout/',                views.logout),
    path('admin/',                       admin.site.urls),

    path('workers/',                     include('workers.urls')),
    path('documents/',                   include('documents.urls')),
    path('contacts/',                    include('contacts.urls')),
    path('archives/',                    include('archives.urls')),

    path('',                             views.page_index),
]
