import csv
from faker import Faker
from datetime import datetime
import random

class AlertCasesDataGenerator:
    def __init__(self, record_count, employee_ids, alert_type_ids, criticity_ids, category_ids):
        self.record_count = record_count
        self.employee_ids = employee_ids
        self.alert_type_ids = alert_type_ids
        self.criticity_ids = criticity_ids
        self.category_ids = category_ids
        self.fake = Faker()

    def generate_data(self):
        with open('csvs\AlertCasesEMPL.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Escribir los encabezados de las columnas
            writer.writerow([
                'nAlertCaseID', 'lAlertTypeID', 'sCustID', 'sAlertComments', 'nCriticityID', 'nStatus', 
                'nCategoryID', 'ID_Usuario', 'ID_Tipo_Documento', 'sGroupSysID', 'ID_Perfil_Supervisor', 
                'dtDateCreated', 'dtDateModified', 'dtDateClosed', 'mTotalDeb', 'mTotalCred', 'iCantDeb', 
                'iCantCred', 'nBranchID'
            ])

            for _ in range(self.record_count):
                writer.writerow([
                    self.fake.unique.random_int(min=1, max=99999),  # nAlertCaseID
                    random.choice(self.alert_type_ids),            # lAlertTypeID
                    random.choice(self.employee_ids),              # sCustID (sEmploID de tblEmployees)
                    self.fake.text(max_nb_chars=2000),             # sAlertComments
                    random.choice(self.criticity_ids),             # nCriticityID
                    self.fake.random_int(min=1, max=10),           # nStatus
                    random.choice(self.category_ids),              # nCategoryID
                    self.fake.user_name()[:20],                    # ID_Usuario
                    self.fake.bothify(text='??#')[:3],             # ID_Tipo_Documento
                    self.fake.random_int(min=1, max=99999),        # sGroupSysID
                    self.fake.user_name()[:20],                    # ID_Perfil_Supervisor
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # dtDateCreated
                    self.fake.date_time_this_century().strftime('%Y-%m-%d %H:%M:%S'),  # dtDateModified
                    self.fake.date_time_this_century().strftime('%Y-%m-%d %H:%M:%S'),  # dtDateClosed
                    round(self.fake.random_number(digits=5), 4),   # mTotalDeb
                    round(self.fake.random_number(digits=5), 4),   # mTotalCred
                    self.fake.random_digit(),                      # iCantDeb
                    self.fake.random_digit(),                      # iCantCred
                    self.fake.random_int(min=1, max=99999)         # nBranchID
                ])

# Uso de la clase
record_count = 200  # Cantidad de registros a generar
employee_ids = [f'emp_{i}' for i in range(100)]  # Suponiendo 100 IDs de empleados
alert_type_ids = [i for i in range(1, 101)]  # Suponiendo 100 IDs de tipos de alerta
criticity_ids = [i for i in range(1, 51)]  # Suponiendo 50 IDs de criticidad
category_ids = [i for i in range(1, 51)]  # Suponiendo 50 IDs de categorías
generator = AlertCasesDataGenerator(record_count, employee_ids, alert_type_ids, criticity_ids, category_ids)
generator.generate_data()