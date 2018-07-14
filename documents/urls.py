from django.urls import path
from EIS import settings
from . import views

# /documents - список документов
# /documents/edit/<num> - редактирование
# /documents/view/<num> - просмотр
# /documents/new - создание

urlpatterns = [
	path('',               views.page_documents),
	path('new/',           views.page_document_new),
	path('view/<int:pk>/', views.page_document_view),
	path('edit/<int:pk>/', views.page_document_edit),
]