from django.shortcuts import render
from EIS.global_info import *


def page_index(request):
	return render(request, 'index.html', {'EIS_NAME': EIS_NAME, 'EIS_VERSION': EIS_VERSION})
