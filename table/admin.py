from django.contrib import admin
from table.models import TableColumn, CSVFilePath


@admin.register(TableColumn)
class TableColumnAdmin(admin.ModelAdmin):
    pass

@admin.register(CSVFilePath)
class CSVFilePathAdmin(admin.ModelAdmin):
    pass
