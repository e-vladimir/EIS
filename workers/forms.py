from django import forms

from .models import EIS_Worker


class WorkerForm(forms.ModelForm):
	class Meta:
		model = EIS_Worker
		fields = ['category', 'post', 'name', 'phone_mobile', 'phone', 'email', 'note']
