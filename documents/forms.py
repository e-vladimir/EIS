from django import forms

from .models import EIS_Document


class DocumentForm(forms.ModelForm):
	class Meta:
		model = EIS_Document
		fields = ['category', 'name', 'date', 'file_pdf', 'file', 'note']