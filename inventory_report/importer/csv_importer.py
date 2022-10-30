import csv
from .importer import Importer


class CsvImporter(Importer):

    @staticmethod
    def import_data(path):
        if ".csv" not in path:
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            content = csv.DictReader(file)
            info = [row for row in content]

            return info
