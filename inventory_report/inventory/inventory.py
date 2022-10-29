from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from .import_functions.import_funtions import (
    import_csv, import_json, import_xml
)


class Inventory:

    @staticmethod
    def create_report(path, type):
        if ".csv" in path:
            data = import_csv(path)
        elif ".json" in path:
            data = import_json(path)
        else:
            data = import_xml(path)

        if type == "simples":
            report = SimpleReport.generate(data)
        elif type == "completo":
            report = CompleteReport.generate(data)
        else:
            raise TypeError

        return report
