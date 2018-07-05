from django import forms

from .models import EIS_Archive


class ArchiveForm(forms.ModelForm):
	class Meta:
		model = EIS_Archive
		fields = ['period_year', 'period_month', 'category', 'name', 'note', 'file_in_pdf', 'file_in']

	def __init__(self, *args, **kwargs):
		super(ArchiveForm, self).__init__(*args, **kwargs)
