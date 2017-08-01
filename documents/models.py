from django.db import models


class EIS_Document(models.Model):
	category    = models.CharField(max_length=100)
	subcategory = models.CharField(max_length=150, blank=True)
	name        = models.CharField(max_length=200)

	date        = models.DateField()

	file_pdf    = models.FileField(blank=True)
	file        = models.FileField(blank=True)

	note        = models.TextField(blank=True)
