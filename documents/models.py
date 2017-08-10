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

	def get_pdf_size(self):
		if self.file_pdf is not None:
			try:
				size = self.file_pdf.size

				if size > 1000:
					return "{0} Kb".format(size // 1000)
				elif size > 1000000:
					return "{0} Mb".format(size // 1000000)
				else:
					return "{0} b".format(size)

			except:
				return "Ошибка"
		else:
			return ""

	def get_size(self):
		if self.file_pdf is not None:
			try:
				size = self.file_pdf.size

				if size > 1000:
					return "{0} Kb".format(size // 1000)
				elif size > 1000000:
					return "{0} Mb".format(size // 1000000)
				else:
					return "{0} b".format(size)

			except:
				return "Ошибка"
		else:
			return ""

	def get_extension(self):
		if self.file is not None:
			try:
				ext = self.file.name[-3:]

				return ext.upper()
			except:
				return "Ошибка"
		else:
			return ""

