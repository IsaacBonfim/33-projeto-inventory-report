import xmltodict
from .importer import Importer


class XmlImporter(Importer):

    @staticmethod
    def import_data(path):
        if ".xml" not in path:
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            content = file.read()
            info = [
                row
                for row in xmltodict.parse(content)["dataset"]["record"]
            ]

            return info
