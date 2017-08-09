import os
from wsgiref.util import FileWrapper

from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib import auth

from EIS import settings
from EIS.global_info import *


def page_index(request):
	if request.user.is_authenticated():
		return render(request, 'index_private.html', {'EIS_NAME': EIS_NAME, 'EIS_VERSION': EIS_VERSION})
	else:
		return render(request, 'index_public.html', {'EIS_NAME': EIS_NAME, 'EIS_VERSION': EIS_VERSION})


def logout(request):
	auth.logout(request)

	return page_index(request)


def pdf_download(request, filename):
	f = open(os.path.join(settings.MEDIA_ROOT, 'pdf', filename), "rb")

	response = HttpResponse(FileWrapper(f), content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=' + filename

	f.close()

	return response


def file_download(request, filename):
	f = open(os.path.join(settings.MEDIA_ROOT, 'file', filename), "rb")

	response = HttpResponse(FileWrapper(f), content_type='application/force-download')
	response['Content-Disposition'] = 'attachment; filename=' + filename

	f.close()

	return response
