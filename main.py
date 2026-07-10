from src.collect import recuperer_agences
from src.export import exporter_excel


agences = recuperer_agences()

exporter_excel(agences)