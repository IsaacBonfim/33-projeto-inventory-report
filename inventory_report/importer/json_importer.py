import json
from .importer import Importer


class JsonImporter(Importer):

    @staticmethod
    def import_data(path):
        if ".json" not in path:
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            content = json.load(file)
            info = [row for row in content]

            return info
