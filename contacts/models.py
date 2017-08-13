from django.db import models


class EIS_Contact(models.Model):
	organization = models.CharField(max_length=100)
	post         = models.CharField(max_length=100)

	name         = models.CharField(max_length=100)

	phone_mobile = models.CharField(max_length=50, blank=True)
	phone        = models.CharField(max_length=50, blank=True)
	email        = models.EmailField(blank=True)

	location     = models.CharField(max_length=200, blank=True)

	note         = models.TextField(blank=True)

	def __str__(self):
		return "{0}/{1}/{2}".format(self.organization, self.post, self.name)
