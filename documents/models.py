import os
from django.db import models
from django.dispatch import receiver
from django.utils import timezone

DOCS_CATEGORIES = [
	'История техникума',
	'Инженерная документация',
	'Коды и информация',
	'Лицензии и аккредитации',
	'Локальные положения',
	'Наблюдательный совет',
	'Свидетельства',
	'Технические документы',
	'Учредительные документы',
	'Шаблоны документов',
	]

LIST_CATEGORIES = ((item, item) for item in DOCS_CATEGORIES)


def rename_upload(instance, filename, folder):
	ext = filename.split('.')
	filename = "%s/%s %s.%s" % (folder, ext[0], timezone.datetime.now().strftime("%Y-%m-%d"), ext[-1])
	return filename


def rename_upload_file(instance, filename):
	return rename_upload(instance, filename, "file")


def rename_upload_pdf(instance, filename):
	return rename_upload(instance, filename, "pdf")


class EIS_Document(models.Model):
	category    = models.CharField(max_length=100, choices=LIST_CATEGORIES)
	name        = models.CharField(max_length=200)

	date        = models.CharField(max_length=50, blank=True)

	file_pdf    = models.FileField(blank=True, upload_to=rename_upload_pdf)
	file        = models.FileField(blank=True, upload_to=rename_upload_file)

	note        = models.TextField(blank=True)

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


@receiver(models.signals.pre_save, sender=EIS_Document)
def auto_delete_file_on_change(sender, instance, **kwargs):
	if not instance.pk:
		return False

	try:
		old_file = EIS_Document.objects.get(pk=instance.pk).file
		old_pdf = EIS_Document.objects.get(pk=instance.pk).file_pdf
	except EIS_Document.DoesNotExist:
		return False

	new_file = instance.file
	new_pdf = instance.file_pdf

	try:
		if not old_file == new_file:
			if os.path.isfile(old_file.path):
				os.remove(old_file.path)
	except:
		pass

	try:
		if not old_pdf == new_pdf:
			if os.path.isfile(old_pdf.path):
				os.remove(old_pdf.path)
	except:
		pass


@receiver(models.signals.post_delete, sender=EIS_Document)
def auto_delete_file_on_delete(sender, instance, **kwargs):
	if instance.file:
		if os.path.isfile(instance.file.path):
			os.remove(instance.file.path)
