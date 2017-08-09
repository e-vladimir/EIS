from django.conf.urls import url
from EIS import settings
from . import views

# /documents - список документов
# /documents/edit/<num> - редактирование
# /documents/view/<num> - просмотр
# /documents/new - создание

urlpatterns = [
	url(r'^$', views.page_documents, name='page_documents'),
	url(r'^new/', views.page_document_new, name='page_document_new'),
	]