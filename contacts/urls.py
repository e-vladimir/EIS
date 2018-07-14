from django.urls import path
from EIS import settings
from . import views

# /contacts - список документов
# /contacts/edit/<num> - редактирование
# /contacts/view/<num> - просмотр
# /contacts/new - создание

urlpatterns = [
	path('',               views.page_contacts),
	path('new/',           views.page_contact_new),
	path('view/<int:pk>/', views.page_contact_view),
	path('edit/<int:pk>/', views.page_contact_edit),
]
