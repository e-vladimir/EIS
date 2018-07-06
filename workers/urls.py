from django.urls import path
from EIS import settings
from . import views

# /workers - список документов
# /workers/edit/<num> - редактирование
# /workers/view/<num> - просмотр
# /workers/new - создание

urlpatterns = [
	path('',               views.page_workers),
	path('new/',           views.page_worker_new),
	path('view/<int:pk>/', views.page_worker_view),
	path('edit/<int:pk>/', views.page_worker_edit),
]
