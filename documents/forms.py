from django import forms

from .models import EIS_Document


class DocumentForm(forms.ModelForm):
	class Meta:
		model = EIS_Document
		fields = ['category', 'name', 'date', 'file_pdf', 'file', 'note']

	def __init__(self, *args, **kwargs):
		super(DocumentForm, self).__init__(*args, **kwargs)
		self.fields['date'].widget = forms.TextInput(attrs={
			'placeholder': '00 месяц 2017'})