from django import forms

from .models import EIS_Worker


class WorkerForm(forms.ModelForm):
	class Meta:
		model = EIS_Worker
		fields = ['organization', 'post', 'name', 'phone_mobile', 'phone', 'location', 'email', 'note']
