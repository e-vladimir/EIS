from django import forms

from .models import EIS_Archive


class ArchiveForm(forms.ModelForm):
	class Meta:
		model = EIS_Archive
		fields = ['period_year', 'period_month', 'category', 'description', 'note', 'file_pdf', 'file']
