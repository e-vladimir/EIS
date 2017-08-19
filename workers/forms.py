from django import forms

from .models import EIS_Worker


class WorkerForm(forms.ModelForm):
	class Meta:
		model = EIS_Worker
		fields = ['category', 'post', 'name', 'phone_mobile', 'phone', 'email', 'note']

	def __init__(self, *args, **kwargs):
		super(WorkerForm, self).__init__(*args, **kwargs)
		self.fields['phone_mobile'].widget = forms.TextInput(attrs={'placeholder': '+7 (___) ___-__-__'})
		self.fields['phone'].widget = forms.TextInput(attrs={'placeholder': '+7 (____) __-__-__'})
		self.fields['email'].widget = forms.TextInput(attrs={'placeholder': '<адрес>@<домен>.ru'})
