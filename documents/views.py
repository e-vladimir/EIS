from django.shortcuts import render
from django.contrib import auth
from EIS.global_info import *
from .models import EIS_Document


def page_documents(request):
	if request.user.is_authenticated():
		return render(request, 'documents.html', {'EIS_NAME': EIS_NAME, 'EIS_VERSION': EIS_VERSION})
	else:
		return render(request, 'index_public.html', {'EIS_NAME': EIS_NAME, 'EIS_VERSION': EIS_VERSION})


def page_document_new(request):
	pass
