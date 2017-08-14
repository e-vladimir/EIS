from django.db import models


class EIS_Worker(models.Model):
	category     = models.CharField(max_length=100)
	post         = models.CharField(max_length=100)

	name         = models.CharField(max_length=100)

	phone_mobile = models.CharField(max_length=50, blank=True)
	phone        = models.CharField(max_length=50, blank=True)

	email        = models.EmailField(blank=True)

	note         = models.TextField(blank=True)

	def __str__(self):
		return "{0} - {1}".format(self.post, self.name)
