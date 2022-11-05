from typing import Iterable
from .inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):

    def __init__(self, importer) -> None:
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        report = self.importer.import_data(path)

        for row in report:
            self.data.append(row)

    def __iter__(self):
        return InventoryIterator(self.data)
