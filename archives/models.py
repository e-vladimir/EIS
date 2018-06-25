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
	period          = models.CharField(default="Месяц Год", blank=True)
	category        = models.CharField(default="Без категории")
	name            = models.CharField()

	tags            = models.TextField(blank=True)

	file_in_pdf     = models.FileField(blank=True)
	file_in         = models.FileField(blank=True)
	file_answer_pdf = models.FileField(blank=True)
	file_answer     = models.FileField(blank=True)

	update_user     = models.CharField(max_length=200, default="Аноним")
	update_date     = models.DateTimeField(null=True, blank=True)
