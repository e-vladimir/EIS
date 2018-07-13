from django.urls import path
from EIS import settings
from . import views

# /archives - список документов
# /archives/period/<period> - список документов за указанный период
# /archives/category/<category> - список документов в категории
# /archives/edit/<num> - редактирование
# /archives/view/<num> - просмотр
# /archives/new - создание

urlpatterns = [
	path('',                                              views.page_archives),

	path('filter/<int:year>/',                            views.page_archives_filter),
	path('filter/<int:year>/<str:category>',              views.page_archives_filter),
	path('filter/<int:year>/<int:month>/',                views.page_archives_filter),
	path('filter/<int:year>/<int:month>/<str:category>/', views.page_archives_filter),

	path('filter/<str:category>/',                        views.page_archives_filter),

	path('new/',                                          views.page_archive_new),
]
