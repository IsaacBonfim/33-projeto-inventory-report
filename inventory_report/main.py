import sys
from .inventory.inventory_refactor import InventoryRefactor
from .reports.simple_report import SimpleReport
from .reports.complete_report import CompleteReport
from .importer import (csv_importer, json_importer, xml_importer)


def main():
    args = sys.argv

    if len(args) < 3:
        print('Verifique os argumentos', file=sys.stderr)
        return

    _, path, type = args

    if ".csv" in path:
        importer = csv_importer.CsvImporter
    elif ".json" in path:
        importer = json_importer.JsonImporter
    else:
        importer = xml_importer.XmlImporter

    info = InventoryRefactor(importer)

    info.import_data(path, type)

    list = info.data

    if type == "simples":
        report = SimpleReport
    else:
        report = CompleteReport

    print(report.generate(list), end='')
