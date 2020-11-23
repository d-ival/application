from django.core.management.base import BaseCommand, CommandError

from table.models import TableColumn, CSVFilePath

DEFAULT_COLUMNS = [
    {'name': 'id', 'width': 1},
    {'name': 'name', 'width': 3},
    {'name': 'price', 'width': 2},
    {'name': 'release_date', 'width': 2},
    {'name': 'lte_exists', 'width': 1},
]


class Command(BaseCommand):
    help = 'Создаёт колонки таблицы по умолчанию и устанавливает имя файла для вывода в таблицу'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        CSVFilePath.set_path('phones.csv')

        if TableColumn.objects.count() != 0:
            raise CommandError(
                'Таблица TableColumn уже содержит строки и не может быть заполнена значениями по умолчанию')
        for column in DEFAULT_COLUMNS:
            column['num'] = DEFAULT_COLUMNS.index(column) + 1
            TableColumn.objects.create(**column)
