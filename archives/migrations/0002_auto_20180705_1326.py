# Generated by Django 2.0.6 on 2018-07-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eis_archive',
            old_name='file_in',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='eis_archive',
            old_name='file_in_pdf',
            new_name='file_pdf',
        ),
        migrations.RemoveField(
            model_name='eis_archive',
            name='tags',
        ),
        migrations.AlterField(
            model_name='eis_archive',
            name='category',
            field=models.CharField(choices=[('Акты проверок', 'Акты проверок'), ('Без категории', 'Без категории'), ('Договора', 'Договора'), ('Докладные', 'Докладные'), ('Документация', 'Документация'), ('Заявки', 'Заявки'), ('Заявления', 'Заявления'), ('Коммерческие предложения', 'Коммерческие предложения'), ('Локальные акты', 'Локальные акты'), ('Отчёты', 'Отчёты'), ('Письма', 'Письма'), ('Постановления', 'Постановления'), ('Предложения', 'Предложения'), ('Предписания', 'Предписания'), ('Приказы', 'Приказы'), ('Протокола', 'Протокола'), ('Распоряжения', 'Распоряжения'), ('Сметы', 'Сметы'), ('Соглашения', 'Соглашения'), ('Уведомления', 'Уведомления'), ('Шаблоны документов', 'Шаблоны документов')], default='Без категории', max_length=100),
        ),
        migrations.AlterField(
            model_name='eis_archive',
            name='note',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='eis_archive',
            name='period_month',
            field=models.CharField(blank=True, choices=[('01', 'Январь'), ('02', 'Февраль'), ('03', 'Март'), ('04', 'Апрель'), ('05', 'Май'), ('06', 'Июнь'), ('07', 'Июль'), ('08', 'Август'), ('09', 'Сентябрь'), ('10', 'Октябрь'), ('11', 'Ноябрь'), ('12', 'Декабрь')], default='Месяц', max_length=30),
        ),
        migrations.AlterField(
            model_name='eis_archive',
            name='period_year',
            field=models.CharField(choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018)], default='Год', max_length=4),
        ),
    ]
