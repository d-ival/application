from django.conf import settings
from django.db import models


class TableColumn(models.Model):

    name = models.CharField(max_length=200, verbose_name='Наименование')
    width = models.SmallIntegerField(verbose_name='Ширина')
    num = models.SmallIntegerField(verbose_name='Порядковый номер')

    class Meta:
        verbose_name = 'Колонка таблицы'
        verbose_name_plural = 'Колонки таблицы'
        ordering = ('num',)

    def __str__(self):
        return f"{self.name} ({self.num})"


class CSVFilePath(models.Model):

    filepath = models.FileField()

    class Meta:
        verbose_name = 'csv-файл'
        verbose_name_plural = 'csv-файлы'

    @classmethod
    def get_path(cls):
        instance = CSVFilePath.objects.first()
        if instance:
            return instance.filepath.name
        else:
            return None

    @classmethod
    def set_path(cls, filepath:str):
        instance = CSVFilePath.objects.first()
        if instance:
            instance.filepath = filepath
            instance.save()
        else:
            CSVFilePath.objects.create(filepath=filepath)

    def __str__(self):
        return self.filepath.name

