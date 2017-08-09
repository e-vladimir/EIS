import os
from wsgiref.util import FileWrapper

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect
from django.utils import timezone

from EIS.global_info import *
from EIS import settings
from .models import EIS_Document
from .forms import DocumentForm


def page_documents(request):
	if request.user.is_authenticated():
		documents = EIS_Document.objects.all().order_by("category", "name")
		return render(request, 'documents.html', {'EIS_NAME': EIS_NAME, 'EIS_VERSION': EIS_VERSION, 'documents': documents})
	else:
		return render(request, 'index_public.html', {'EIS_NAME': EIS_NAME, 'EIS_VERSION': EIS_VERSION})


def page_document_view(request):
	pass


def page_document_edit(request):
	pass


def page_document_new(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = DocumentForm(request.POST, request.FILES)

			if form.is_valid():
				document = form.save(commit=False)
				document.update_user = "{0} {1}".format(request.user.first_name, request.user.last_name)
				document.update_date = timezone.now()

				document.save()

				return redirect('page_documents')
			else:
				print('Not valid!', form.errors)
				return ""
		else:
			form = DocumentForm()
			return render(request, 'new.html', {'EIS_NAME': EIS_NAME, 'EIS_VERSION': EIS_VERSION, 'form': form})
	else:
		return render(request, 'index_public.html', {'EIS_NAME': EIS_NAME, 'EIS_VERSION': EIS_VERSION})
