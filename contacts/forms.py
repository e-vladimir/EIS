from django import forms

from .models import EIS_Contact


class ContactForm(forms.ModelForm):
	class Meta:
		model = EIS_Contact
		fields = ['organization', 'post', 'name', 'phone_mobile', 'phone', 'location', 'email', 'note']
