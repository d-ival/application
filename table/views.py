from django.shortcuts import render
from rest_framework.response import Response
import csv

from .models import TableColumn, CSVFilePath

def csv_to_table(filename):

    table = []
    if not filename:
        return table

    try:
        with open(filename, 'rt') as csv_file:
            header = []

            table_reader = csv.reader(csv_file, delimiter=';')
            for table_row in table_reader:
                if not header:
                    header = {idx: value for idx, value in enumerate(table_row)}
                else:
                    row = {header.get(idx) or 'col{:03d}'.format(idx): value
                           for idx, value in enumerate(table_row)}
                    table.append(row)
    except FileExistsError as fe_err:
        pass
    except csv.Error as csv_err:
        pass

    return table


def table_view(request):
    template = 'table.html'
    columns = TableColumn.objects.all()
    csv_filename = CSVFilePath.get_path()

    table = csv_to_table(csv_filename)

    context = {
        'columns': columns,
        'table': table,
        'csv_file': csv_filename
    }
    result = render(request, template, context)
    return result
