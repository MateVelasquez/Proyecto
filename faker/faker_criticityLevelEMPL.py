import csv
from faker import Faker
from datetime import datetime

class CriticityLevelDataGenerator:
    def __init__(self, record_count):
        self.record_count = record_count
        self.fake = Faker()

    def generate_data(self):
        with open('csvs\criticityLevelEMPL.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Escribir los encabezados de las columnas
            writer.writerow([
                'nCriticityID', 'sName', 'sDescription', 'sValue', 'cantDiasResolucion',
                'bStatus', 'dtDateCreated', 'dtDateModified'
            ])

            for _ in range(self.record_count):
                writer.writerow([
                    self.fake.unique.random_int(min=1, max=99999),  # nCriticityID
                    self.fake.word()[:50],                          # sName
                    self.fake.sentence()[:200],                     # sDescription
                    self.fake.word()[:50],                          # sValue
                    self.fake.random_int(min=1, max=30),            # cantDiasResolucion
                    self.fake.boolean(),                            # bStatus
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),   # dtDateCreated
                    self.fake.date_time_this_century().strftime('%Y-%m-%d %H:%M:%S')  # dtDateModified
                ])

# Uso de la clase
record_count = 50  # Cantidad de registros a generar
generator = CriticityLevelDataGenerator(record_count)
generator.generate_data()