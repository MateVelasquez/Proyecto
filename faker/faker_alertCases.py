import csv
import pandas as pd
from faker import Faker
from datetime import datetime
import random

class AlertCasesDataGenerator:
    def __init__(self, record_count):
        self.record_count = record_count
        self.fake = Faker()

    def read_ids_from_csv(self, filename):
        data = pd.read_csv(filename)
        return data.iloc[:, 0].tolist()  # Asume que el primer campo es el ID

    def generate_data(self, customer_ids, alert_type_ids, criticity_ids, category_ids):
        with open('csvs\AlertCases.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                'nAlertCaseID', 'lAlertTypeID', 'sCustID', 'sAlertComments', 'nCriticityID', 'nStatus',
                'nCategoryID', 'ID_Usuario', 'ID_Tipo_Documento', 'sGroupSysID', 'ID_Perfil_Supervisor',
                'dtDateCreated', 'dtDateModified', 'dtDateClosed', 'mTotalDeb', 'mTotalCred', 'iCantDeb',
                'iCantCred', 'nBranchID'
            ])

            for _ in range(self.record_count):
                writer.writerow([
                    self.fake.unique.random_int(min=1, max=99999),  # nAlertCaseID
                    random.choice(alert_type_ids),  # lAlertTypeID
                    random.choice(customer_ids),    # sCustID
                    self.fake.text(max_nb_chars=2000),  # sAlertComments
                    random.choice(criticity_ids),   # nCriticityID
                    self.fake.random_int(min=1, max=10),  # nStatus
                    random.choice(category_ids),    # nCategoryID
                    self.fake.user_name()[:20],     # ID_Usuario
                    self.fake.bothify(text='??#')[:3],  # ID_Tipo_Documento
                    self.fake.random_int(min=1, max=99999),  # sGroupSysID
                    self.fake.user_name()[:20],     # ID_Perfil_Supervisor
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # dtDateCreated
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # dtDateModified
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # dtDateClosed
                    round(self.fake.random_number(digits=5), 4),  # mTotalDeb
                    round(self.fake.random_number(digits=5), 4),  # mTotalCred
                    self.fake.random_digit(),  # iCantDeb
                    self.fake.random_digit(),  # iCantCred
                    self.fake.random_int(min=1, max=99999)  # nBranchID
                ])

# Uso de la clase
record_count = 200
generator = AlertCasesDataGenerator(record_count)

# Leer los IDs desde los archivos CSV
customer_ids = generator.read_ids_from_csv('csvs\customers.csv')
alert_type_ids = generator.read_ids_from_csv('csvs\AlertTypes.csv')
criticity_ids = generator.read_ids_from_csv('csvs\criticityLevel.csv')
category_ids = generator.read_ids_from_csv('csvs\caseCategory.csv')

# Generar los datos
generator.generate_data(customer_ids, alert_type_ids, criticity_ids, category_ids)