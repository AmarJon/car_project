import csv
import numpy as np

class CSVExporter:
    def __init__(self):
        pass

    def export_list(self, exportable_list):
        a = np.array(exportable_list)
        np.savetxt('output.csv', a, delimiter=',', fmt='%s')
