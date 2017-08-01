from django.shortcuts import render
from django.contrib import auth
from EIS.global_info import *


def page_index(request):
	if request.user.is_authenticated():
		return render(request, 'index_private.html', {'EIS_NAME': EIS_NAME, 'EIS_VERSION': EIS_VERSION})
	else:
		return render(request, 'index_public.html', {'EIS_NAME': EIS_NAME, 'EIS_VERSION': EIS_VERSION})


def logout(request):
	auth.logout(request)

	return page_index(request)
