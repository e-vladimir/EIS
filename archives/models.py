from django.db import models


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

ARCHIVES_YEARS = [year for year in range(2010, 2019)]

LIST_CATEGORIES = ((item, item) for item in ARCHIVES_CATEGORIES)
LIST_YEARS = ((item, item) for item in ARCHIVES_YEARS)
LIST_MONTH = (("01", "Январь"),
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


class EIS_Archive(models.Model):
	period_year     = models.CharField(default="Год", max_length=4, choices=LIST_YEARS)
	period_month    = models.CharField(default="Месяц", blank=True, max_length=30, choices=LIST_MONTH)

	category        = models.CharField(default="Без категории", max_length=100, choices=LIST_CATEGORIES)
	name            = models.CharField(null=False, max_length=200)

	note            = models.CharField(blank=True, max_length=250)

	file_in_pdf     = models.FileField(blank=True)
	file_in         = models.FileField(blank=True)

	update_user     = models.CharField(max_length=200, default="Аноним")
	update_date     = models.DateTimeField(null=True, blank=True)
