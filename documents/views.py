import os
from wsgiref.util import FileWrapper

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.shortcuts import redirect
from django.utils import timezone

from EIS.global_info import *
from EIS import settings
from .models import EIS_Document
from .forms import DocumentForm


def page_documents(request):
	EIS_info = dict()
	EIS_info['name'] = EIS_NAME
	EIS_info['version'] = EIS_VERSION

	if request.user.is_authenticated():
		documents = EIS_Document.objects.all().order_by("category", "name")

		EIS_info['title'] = "ДОКУМЕНТЫ"
		EIS_info['user'] = "{0} {1}".format(request.user.first_name, request.user.last_name)

		return render(request, 'documents.html', {'EIS_info': EIS_info, 'documents': documents})
	else:
		return render(request, 'index_public.html', {'EIS_info': EIS_info})


def page_document_view(request, pk):
	EIS_info = dict()
	EIS_info['name'] = EIS_NAME
	EIS_info['version'] = EIS_VERSION

	if request.user.is_authenticated():
		document = get_object_or_404(EIS_Document, pk=pk)

		EIS_info['title'] = "ДОКУМЕНТЫ / " + document.category
		EIS_info['user'] = "{0} {1}".format(request.user.first_name, request.user.last_name)

		return render(request, 'view.html', {'EIS_info': EIS_info, 'document': document})
	else:
		return render(request, 'index_public.html', {'EIS_info': EIS_info})


def page_document_edit(request, pk):
	EIS_info = dict()
	EIS_info['name'] = EIS_NAME
	EIS_info['version'] = EIS_VERSION

	if request.user.is_authenticated():
		document = get_object_or_404(EIS_Document, pk=pk)

		EIS_info['title'] = "ДОКУМЕНТЫ / " + document.category
		EIS_info['user'] = "{0} {1}".format(request.user.first_name, request.user.last_name)

		if request.method == "POST":
			form = DocumentForm(request.POST, request.FILES, instance=document)

			if form.is_valid():
				document = form.save(commit=False)
				document.update_user = "{0} {1}".format(request.user.first_name, request.user.last_name)
				document.update_date = timezone.now()

				document.save()

				return redirect('page_document_view', pk)
		else:
			form = DocumentForm(instance=document)
			return render(request, 'new.html', {'EIS_info': EIS_info, 'form': form})
	else:
		return render(request, 'index_public.html', {'EIS_info': EIS_info})


def page_document_new(request):
	EIS_info = dict()
	EIS_info['name'] = EIS_NAME
	EIS_info['version'] = EIS_VERSION

	if request.user.is_authenticated():
		EIS_info['title'] = "ДОКУМЕНТЫ / Новый документ"
		EIS_info['user'] = "{0} {1}".format(request.user.first_name, request.user.last_name)

		if request.method == "POST":
			form = DocumentForm(request.POST, request.FILES)

			if form.is_valid():
				document = form.save(commit=False)
				document.update_user = "{0} {1}".format(request.user.first_name, request.user.last_name)
				document.update_date = timezone.now()

				document.save()

				return redirect('page_documents')
		else:
			form = DocumentForm()
			return render(request, 'new.html', {'EIS_info': EIS_info, 'form': form})
	else:
		return render(request, 'index_public.html', {'EIS_info': EIS_info})
