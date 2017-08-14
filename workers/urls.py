from django.conf.urls import url
from EIS import settings
from . import views

# /workers - список документов
# /workers/edit/<num> - редактирование
# /workers/view/<num> - просмотр
# /workers/new - создание

urlpatterns = [
	url(r'^$', views.page_workers, name='page_workers'),
	url(r'^new/', views.page_worker_new, name='page_worker_new'),
	url(r'^view/(?P<pk>[0-9]+)/$', views.page_worker_view, name='page_worker_view'),
	url(r'^edit/(?P<pk>[0-9]+)/$', views.page_worker_edit, name='page_worker_edit'),
]
