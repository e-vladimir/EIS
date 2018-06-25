from django.conf.urls import url
from EIS import settings
from . import views

# /archives - список документов
# /archives/edit/<num> - редактирование
# /archives/view/<num> - просмотр
# /archives/new - создание

# urlpatterns = [
# 	url(r'^$', views.page_contacts, name='page_contacts'),
# 	url(r'^new/', views.page_contact_new, name='page_contact_new'),
# 	url(r'^view/(?P<pk>[0-9]+)/$', views.page_contact_view, name='page_contact_view'),
# 	url(r'^edit/(?P<pk>[0-9]+)/$', views.page_contact_edit, name='page_contact_edit'),
# ]
