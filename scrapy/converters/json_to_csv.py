from scrapy.exporters import CsvItemExporter
import json

with open('20-40.json', 'r') as file:
    items = json.loads(file.read())

common_keys = set(k for r in items for k in r)

file = open('ym_items_2000-4000.csv', 'w+b')
exporter = CsvItemExporter(file)
exporter.fields_to_export = list(common_keys)
exporter.start_exporting()

for item in items:
    exporter.export_item(item)

exporter.finish_exporting()
file.close()

