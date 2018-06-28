from django.db import models


ARCHIVES_CATEGORIES = [
	"Приказы",
	"Приказы (внешние)",
	"Распоряжения",
	"Локальные акты",

	"Заявки",
	"Заявления",

	"Письма (исходящее)"
	"Письма (входящее)",

	"Докладные",

	"Протоколы",
	"Документация",

	"Сметы",
	"Коммерческие предложения",

	"Договоры",
	"Соглашения",

	"Уведомления",

	"Шаблоны документов",

	"Постановления",
	"Акты проверок",
	"Предписания",
	"Отчёты",
	"Предложения"
]


class EIS_Archive(models.Model):
	period_year     = models.CharField(default="Год",   blank=True, max_length=4)
	period_month    = models.CharField(default="Месяц", blank=True, max_length=10)

	category        = models.CharField(default="Без категории", max_length=100)
	name            = models.CharField(null=False, max_length=200)

	tags            = models.TextField(blank=True)
	note            = models.CharField(blank=True, max_length=200)

	file_in_pdf     = models.FileField(blank=True)
	file_in         = models.FileField(blank=True)

	update_user     = models.CharField(max_length=200, default="Аноним")
	update_date     = models.DateTimeField(null=True, blank=True)
