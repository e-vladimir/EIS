from django.shortcuts import render, get_object_or_404, redirect
from EIS.global_info import *
from .models import EIS_Archive, LIST_MONTH
from .forms import ArchiveForm
from django.utils import timezone


def page_archives(request):
	EIS_info            = dict()
	EIS_info['name']    = EIS_NAME
	EIS_info['version'] = EIS_VERSION
	EIS_info['module']  = "Archives"

	if request.user.is_authenticated:
		documents     = EIS_Archive.objects.all().order_by("period_year",
		                                                   "period_month",
		                                                   "category",
		                                                   "description")
		list_year     = []
		list_category = []

		for document in documents:
			doc_year     = document.period_year
			doc_category = document.category

			if doc_year        not in list_year:     list_year.append(doc_year)
			if doc_category    not in list_category: list_category.append(doc_category)

		EIS_info['title'] = "Архив документов"
		EIS_info['user'] = "{0} {1}".format(request.user.first_name, request.user.last_name)

		list_year.sort()
		list_category.sort()

		return render(request, 'archives.html', {'EIS_info'     : EIS_info,
		                                         'list_year'    : list_year,
		                                         'list_category': list_category})
	else:
		return render(request, 'index_public.html', {'EIS_info': EIS_info})


def page_archives_filter(request, year=None, month=None, category=None):
	EIS_info            = dict()
	EIS_info['name']    = EIS_NAME
	EIS_info['version'] = EIS_VERSION
	EIS_info['module']  = "Archives"

	if request.user.is_authenticated:
		EIS_info['title'] = "Архив документов "

		list_month     = []
		list_category  = []
		list_year      = []

		list_documents = []

		documents      = EIS_Archive.objects.all().order_by("period_year",
		                                                    "period_month",
		                                                    "category",
		                                                    "description")

		for document in documents:
			doc_category = str(document.category)
			doc_year     = str(document.period_year)
			doc_month    = str(document.period_month)

			include_doc  = False

			if doc_year not in list_year: list_year.append(doc_year)

			if category is not None:
				include_doc = doc_category == str(category)
			else:
				if year is not None:
					include_doc = doc_year == str(year)

					if include_doc:
						if int(doc_month) not in list_month: list_month.append(int(doc_month))

					if month is not None:
						include_doc = include_doc and (int(doc_month) == int(month))

			if include_doc:
				list_documents.append(document)

		# Фильтры
		list_category.sort()
		list_month.sort()
		list_year.sort()

		if category is not None:
			EIS_info['title'] += "по категории {0} ".format(category)

		if year is not None:
			if month is not None:
				EIS_info['title'] += "за {0} {1} года".format(month, year)
			else:
				EIS_info['title'] += "за {0} год".format(year)

		EIS_info['user'] = "{0} {1}".format(request.user.first_name, request.user.last_name)

		params = {'EIS_info'      : EIS_info,
		          'list_year'     : list_year,
		          'year_current'  : str(year),
		          'category_current': str(category),
		          'list_documents': list_documents,
		          'list_month'    : list_month,
		          'month_current' : month}

		return render(request, 'archives_filter.html', params)
	else:
		return render(request, 'index_public.html', {'EIS_info': EIS_info})


# def page_contact_view(request, pk):
# 	EIS_info = dict()
# 	EIS_info['name']    = EIS_NAME
# 	EIS_info['version'] = EIS_VERSION
# 	EIS_info['module']  = "Contacts"
#
# 	if request.user.is_authenticated:
# 		contact = get_object_or_404(EIS_Contact, pk=pk)
#
# 		EIS_info['title'] = contact.name
# 		EIS_info['subtitle'] = contact.organization
# 		EIS_info['user'] = "{0} {1}".format(request.user.first_name, request.user.last_name)
#
# 		return render(request, 'contact_view.html', {'EIS_info': EIS_info, 'contact': contact})
# 	else:
# 		return render(request, 'index_public.html', {'EIS_info': EIS_info})
#
#
# def page_contact_edit(request, pk):
# 	EIS_info            = dict()
# 	EIS_info['name']    = EIS_NAME
# 	EIS_info['version'] = EIS_VERSION
# 	EIS_info['module']  = "Contacts"
#
# 	if request.user.is_authenticated:
# 		contact = get_object_or_404(EIS_Contact, pk=pk)
#
# 		EIS_info['title'] = contact.name
# 		EIS_info['subtitle'] = "{0}/{1}".format(contact.organization, contact.post)
# 		EIS_info['user'] = "{0} {1}".format(request.user.first_name, request.user.last_name)
#
# 		if request.method == "POST":
# 			form = ContactForm(request.POST, request.FILES, instance=contact)
#
# 			if form.is_valid():
# 				form.save()
#
# 				return redirect('page_contact_view', pk)
# 		else:
# 			form = ContactForm(instance=contact)
# 			return render(request, 'contact_new.html', {'EIS_info': EIS_info, 'form': form})
# 	else:
# 		return render(request, 'index_public.html', {'EIS_info': EIS_info})


def page_archive_new(request):
	EIS_info            = dict()
	EIS_info['name']    = EIS_NAME
	EIS_info['version'] = EIS_VERSION
	EIS_info['module']  = "Archives"

	if request.user.is_authenticated:
		EIS_info['title'] = "Добавление в архив"
		EIS_info['user']  = "{0} {1}".format(request.user.first_name,
		                                    request.user.last_name)

		if request.method == "POST":
			form = ArchiveForm(request.POST,
			                   request.FILES)

			if form.is_valid():
				document             = form.save(commit=False)
				document.update_user = "{0} {1}".format(request.user.first_name,
				                                        request.user.last_name)
				document.update_date = timezone.now()

				form.save()

				return redirect('/archives/')
		else:
			form = ArchiveForm()
			return render(request, 'archive_new.html', {'EIS_info': EIS_info,
			                                            'form'    : form})
	else:
		return render(request, 'index_public.html', {'EIS_info': EIS_info})
