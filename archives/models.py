import os
from django.db import models
from django.dispatch import receiver
from django.utils import timezone


ARCHIVES_CATEGORIES = [
	"Приказы",
	"Распоряжения",
	"Локальные акты",

	"Заявки",
	"Заявления",

	"Письма",

	"Докладные",

	"Протокола",
	"Документация",

	"Сметы",
	"Коммерческие предложения",

	"Договора",
	"Соглашения",

	"Уведомления",

	"Шаблоны документов",

	"Постановления",
	"Акты проверок",
	"Предписания",
	"Отчёты",
	"Предложения",

	"Без категории"]
ARCHIVES_CATEGORIES.sort()

ARCHIVES_YEARS = [str(year) for year in range(2010, 2019)]

LIST_CATEGORIES = ((item, item) for item in ARCHIVES_CATEGORIES)
LIST_YEARS = ((item, item) for item in ARCHIVES_YEARS)
LIST_MONTH = (("00", "Нет данных"),
			  ("01", "Январь"),
              ("02", "Февраль"),
              ("03", "Март"),
              ("04", "Апрель"),
              ("05", "Май"),
              ("06", "Июнь"),
              ("07", "Июль"),
              ("08", "Август"),
              ("09", "Сентябрь"),
              ("10", "Октябрь"),
              ("11", "Ноябрь"),
              ("12", "Декабрь"),)


def rename_upload(instance, filename, folder):
	ext = filename.split('.')
	filename = "%s/%s %s.%s" % (folder, ext[0], timezone.datetime.now().strftime("%Y-%m-%d"), ext[-1])
	return filename


def rename_upload_file(instance, filename):
	return rename_upload(instance, filename, "archive/file")


def rename_upload_pdf(instance, filename):
	return rename_upload(instance, filename, "archive/pdf")


class EIS_Archive(models.Model):
	period_year     = models.CharField(max_length=4, choices=LIST_YEARS)
	period_month    = models.CharField(max_length=30, choices=LIST_MONTH)

	category        = models.CharField(default="Без категории", max_length=100, choices=LIST_CATEGORIES)
	description     = models.CharField(blank=True, default="", max_length=250)

	note            = models.CharField(blank=True, max_length=250)

	file_pdf        = models.FileField(blank=True, upload_to=rename_upload_pdf)
	file            = models.FileField(blank=True, upload_to=rename_upload_file)

	update_user     = models.CharField(max_length=200, default="Аноним")
	update_date     = models.DateTimeField(null=True, blank=True)

	def delete(self, using=None, keep_parents=False):
		self.file.delete()
		self.file_pdf.delete()

		super(EIS_Archive, self).delete(using, keep_parents)

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

	def get_month_str(self):
		return LIST_MONTH[int(self.period_month)][1]


@receiver(models.signals.pre_save, sender=EIS_Archive)
def auto_delete_file_on_change(sender, instance, **kwargs):
	if not instance.pk:
		return False

	try:
		old_file = EIS_Archive.objects.get(pk=instance.pk).file
		old_pdf = EIS_Archive.objects.get(pk=instance.pk).file_pdf
	except EIS_Archive.DoesNotExist:
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


@receiver(models.signals.post_delete, sender=EIS_Archive)
def auto_delete_file_on_delete(sender, instance, **kwargs):
	if instance.file:
		if os.path.isfile(instance.file.path):
			os.remove(instance.file.path)
