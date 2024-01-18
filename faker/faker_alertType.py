import csv
import pandas as pd
from faker import Faker
from datetime import datetime
import random

class AlertTypesDataGenerator:
    def __init__(self, record_count):
        self.record_count = record_count
        self.fake = Faker()

    def read_ids_from_csv(self, filename):
        data = pd.read_csv(filename)
        return data.iloc[:, 0].tolist()  # Asume que el primer campo es el ID

    def generate_data(self, criticity_ids, category_ids):
        with open('csvs\AlertTypes.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                'lAlertTypeID', 'sName', 'sDescription', 'sActionScript', 'nCriticityID',
                'nCategoryID', 'ID_Usuario', 'ID_Tipo_Documento', 'ID_Perfil_Supervisor',
                'sGroupCustID', 'dtCreated', 'dtModified', 'dtStatus'
            ])

            for _ in range(self.record_count):
                writer.writerow([
                    self.fake.unique.random_int(min=1, max=99999),  # lAlertTypeID
                    self.fake.word()[:50],                          # sName
                    self.fake.sentence()[:250],                     # sDescription
                    self.fake.text(max_nb_chars=3000),              # sActionScript
                    random.choice(criticity_ids),                   # nCriticityID
                    random.choice(category_ids),                    # nCategoryID
                    self.fake.user_name()[:20],                     # ID_Usuario
                    self.fake.bothify(text='??#')[:3],              # ID_Tipo_Documento
                    self.fake.user_name()[:20],                     # ID_Perfil_Supervisor
                    self.fake.unique.uuid4()[:50],                  # sGroupCustID
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),   # dtCreated
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),   # dtModified
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')    # dtStatus
                ])

# Uso de la clase
record_count = 100
generator = AlertTypesDataGenerator(record_count)

# Leer los IDs desde los archivos CSV
criticity_ids = generator.read_ids_from_csv('csvs\criticityLevel.csv')
category_ids = generator.read_ids_from_csv('csvs\caseCategory.csv')

# Generar los datos
generator.generate_data(criticity_ids, category_ids)