import csv
import json
import xmltodict


def import_csv(path):
    with open(path) as file:
        content = csv.DictReader(file)
        info = [row for row in content]

        return info


def import_json(path):
    with open(path) as file:
        content = json.load(file)
        info = [row for row in content]

        return info


def import_xml(path):
    with open(path) as file:
        content = file.read()
        info = [
            row for row in xmltodict.parse(content)["dataset"]["record"]
        ]

        return info
