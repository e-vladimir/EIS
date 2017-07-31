from django.shortcuts import render


def page_index(request):
	return render(request, 'index.html', {})
