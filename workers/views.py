from django.shortcuts import render, get_object_or_404, redirect
from EIS.global_info import *
from .forms import WorkerForm
from .models import EIS_Worker


def page_workers(request):
	EIS_info            = dict()
	EIS_info['name']    = EIS_NAME
	EIS_info['version'] = EIS_VERSION
	EIS_info['module']  = "Workers"

	if request.user.is_authenticated:
		workers = EIS_Worker.objects.all().order_by("category", "post", "name")

		EIS_info['title'] = "Список сотрудников"
		EIS_info['user'] = "{0} {1}".format(request.user.first_name, request.user.last_name)

		return render(request, 'workers.html', {'EIS_info': EIS_info, 'workers': workers})
	else:
		return render(request, 'index_public.html', {'EIS_info': EIS_info})


def page_worker_view(request, pk):
	EIS_info            = dict()
	EIS_info['name']    = EIS_NAME
	EIS_info['version'] = EIS_VERSION
	EIS_info['module']  = "Workers"

	if request.user.is_authenticated:
		worker = get_object_or_404(EIS_Worker, pk=pk)

		EIS_info['title'] = worker.name
		EIS_info['subtitle'] = worker.post
		EIS_info['user'] = "{0} {1}".format(request.user.first_name, request.user.last_name)

		return render(request, 'worker_view.html', {'EIS_info': EIS_info, 'worker': worker})
	else:
		return render(request, 'index_public.html', {'EIS_info': EIS_info})


def page_worker_edit(request, pk):
	EIS_info            = dict()
	EIS_info['name']    = EIS_NAME
	EIS_info['version'] = EIS_VERSION
	EIS_info['module']  = "Workers"

	if request.user.is_authenticated:
		worker = get_object_or_404(EIS_Worker, pk=pk)

		EIS_info['title'] = worker.name
		EIS_info['subtitle'] = "{0}".format(worker.post)
		EIS_info['user'] = "{0} {1}".format(request.user.first_name, request.user.last_name)

		if request.method == "POST":
			form = WorkerForm(request.POST, request.FILES, instance=worker)

			if form.is_valid():
				form.save()

				return redirect('/workers/view/{0}'.format(pk))
		else:
			form = WorkerForm(instance=worker)
			return render(request, 'worker_new.html', {'EIS_info': EIS_info, 'form': form})
	else:
		return render(request, 'index_public.html', {'EIS_info': EIS_info})


def page_worker_new(request):
	EIS_info            = dict()
	EIS_info['name']    = EIS_NAME
	EIS_info['version'] = EIS_VERSION

	if request.user.is_authenticated:
		EIS_info['title'] = "Новый сотрудник"
		EIS_info['user'] = "{0} {1}".format(request.user.first_name, request.user.last_name)

		if request.method == "POST":
			form = WorkerForm(request.POST, request.FILES)

			if form.is_valid():
				form.save()

				return redirect('/workers/')
		else:
			form = WorkerForm()
			return render(request, 'worker_new.html', {'EIS_info': EIS_info, 'form': form})
	else:
		return render(request, 'index_public.html', {'EIS_info': EIS_info})
