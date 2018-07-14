from django.urls import path
from EIS import settings
from . import views


urlpatterns = [
	path('',                                              views.page_archives),

	path('filter/<int:year>/',                            views.page_archives_filter),
	path('filter/<int:year>/<int:month>/',                views.page_archives_filter),

	path('filter/<str:category>/',                        views.page_archives_filter),
	path('filter/<str:category>/<int:year>/',             views.page_archives_filter),
	path('filter/<str:category>/<int:year>/<int:month>/', views.page_archives_filter),

	path('new/',                                          views.page_archive_new),

	path('view/<int:pk>/',                                views.page_archive_view),
	path('edit/<int:pk>/',                                views.page_archive_edit),
]
