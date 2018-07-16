from django import template

register = template.Library()


@register.simple_tag
def month_to_str(in_month_num):
	MONTHS = ["Январь",
	          "Февраль",
	          "Март",
	          "Апрель",
	          "Май",
	          "Июнь",
	          "Июль",
	          "Август",
	          "Сентябрь",
	          "Октябрь",
	          "Ноябрь",
	          "Декабрь"]

	if int(in_month_num) in range(1, 13):
		return MONTHS[int(in_month_num) - 1]
	else:
		return ""
