from django.conf.urls import url
from EIS import settings
from . import views

# /archives - список документов
# /archives/period/<period> - список документов за указанный период
# /archives/category/<category> - список документов в категории
# /archives/edit/<num> - редактирование
# /archives/view/<num> - просмотр
# /archives/new - создание

urlpatterns = [
	url(r'^$',    views.page_arvhives,    name='page_archives'),
	url(r'^new/', views.page_archive_new, name='page_archive_new'),
	# url(r'^view/(?P<pk>[0-9]+)/$', views.page_contact_view, name='page_contact_view'),
	# url(r'^edit/(?P<pk>[0-9]+)/$', views.page_contact_edit, name='page_contact_edit'),
]
