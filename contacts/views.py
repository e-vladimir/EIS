from django.shortcuts import render, get_object_or_404, redirect
from EIS.global_info import *
from .forms import ContactForm
from .models import EIS_Contact


def page_contacts(request):
	EIS_info            = dict()
	EIS_info['name']    = EIS_NAME
	EIS_info['version'] = EIS_VERSION
	EIS_info['module']  = "Contacts"

	if request.user.is_authenticated:
		contacts = EIS_Contact.objects.all().order_by("organization", "post", "name")

		EIS_info['title'] = "Список внешних контактов"
		EIS_info['user'] = "{0} {1}".format(request.user.first_name, request.user.last_name)

		return render(request, 'contacts.html', {'EIS_info': EIS_info, 'contacts': contacts})
	else:
		return render(request, 'index_public.html', {'EIS_info': EIS_info})


def page_contact_view(request, pk):
	EIS_info = dict()
	EIS_info['name']    = EIS_NAME
	EIS_info['version'] = EIS_VERSION
	EIS_info['module']  = "Contacts"

	if request.user.is_authenticated:
		contact = get_object_or_404(EIS_Contact, pk=pk)

		EIS_info['title'] = contact.name
		EIS_info['subtitle'] = contact.organization
		EIS_info['user'] = "{0} {1}".format(request.user.first_name, request.user.last_name)

		return render(request, 'contact_view.html', {'EIS_info': EIS_info, 'contact': contact})
	else:
		return render(request, 'index_public.html', {'EIS_info': EIS_info})


def page_contact_edit(request, pk):
	EIS_info            = dict()
	EIS_info['name']    = EIS_NAME
	EIS_info['version'] = EIS_VERSION
	EIS_info['module']  = "Contacts"

	if request.user.is_authenticated:
		contact = get_object_or_404(EIS_Contact, pk=pk)

		EIS_info['title'] = contact.name
		EIS_info['subtitle'] = "{0}/{1}".format(contact.organization, contact.post)
		EIS_info['user'] = "{0} {1}".format(request.user.first_name, request.user.last_name)

		if request.method == "POST":
			form = ContactForm(request.POST, request.FILES, instance=contact)

			if form.is_valid():
				form.save()

				return redirect('page_contact_view', pk)
		else:
			form = ContactForm(instance=contact)
			return render(request, 'contact_new.html', {'EIS_info': EIS_info, 'form': form})
	else:
		return render(request, 'index_public.html', {'EIS_info': EIS_info})


def page_contact_new(request):
	EIS_info            = dict()
	EIS_info['name']    = EIS_NAME
	EIS_info['version'] = EIS_VERSION
	EIS_info['module']  = "Contacts"

	if request.user.is_authenticated:
		EIS_info['title'] = "Новый контакт"
		EIS_info['user'] = "{0} {1}".format(request.user.first_name, request.user.last_name)

		if request.method == "POST":
			form = ContactForm(request.POST, request.FILES)

			if form.is_valid():
				form.save()

				return redirect('page_contacts')
		else:
			form = ContactForm()
			return render(request, 'contact_new.html', {'EIS_info': EIS_info, 'form': form})
	else:
		return render(request, 'index_public.html', {'EIS_info': EIS_info})
