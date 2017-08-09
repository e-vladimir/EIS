from django.db import models
from django.utils import timezone


class EIS_Document(models.Model):
	category    = models.CharField(max_length=100)
	name        = models.CharField(max_length=200)

	date        = models.CharField(max_length=50, blank=True)

	file_pdf    = models.FileField(blank=True, upload_to="pdf/")
	file        = models.FileField(blank=True, upload_to="file/")

	note        = models.TextField(blank=True)

	update_user = models.CharField(max_length=200, default="Аноним")
	update_date = models.DateTimeField(null=True, blank=True)
