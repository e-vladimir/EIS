from django.db import models
from django.utils import timezone

DOCS_CATEGORIES = [
	'История техникума',
	'Коды и информация',
	'Лицензии и аккредитации',
	'Наблюдательный совет',
	'Технические документы',
	'Учредительные документы',
	'Шаблоны документов',
    ]

LIST_CATEGORIES = ((item, item) for item in DOCS_CATEGORIES)


class EIS_Document(models.Model):
	category = models.CharField(max_length=100, choices=LIST_CATEGORIES)
	name = models.CharField(max_length=200)

	date = models.CharField(max_length=50, blank=True)

	file_pdf = models.FileField(blank=True, upload_to="pdf/")
	file = models.FileField(blank=True, upload_to="file/")

	note = models.TextField(blank=True)

	update_user = models.CharField(max_length=200, default="Аноним")
	update_date = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return "{0}/{1}".format(self.category, self.name)

	def delete(self, using=None, keep_parents=False):
		self.file.delete()
		self.file_pdf.delete()

		super(EIS_Document, self).delete(using, keep_parents)

	def file_size(self, in_file):
		if in_file is not None:
			try:
				size = in_file.size

				if size > 1000000:
					return "{0} Mb".format(size // 1000000)
				elif size > 1000:
					return "{0} Kb".format(size // 1000)
				else:
					return "{0} b".format(size)

			except:
				return "Ошибка"
		else:
			return ""

	def get_pdf_size(self):
		return self.file_size(self.file_pdf)

	def get_size(self):
		return self.file_size(self.file)

	def get_extension(self):
		if self.file is not None:
			try:
				ext = self.file.name[-3:]

				return ext.upper()
			except:
				return "Ошибка"
		else:
			return ""
