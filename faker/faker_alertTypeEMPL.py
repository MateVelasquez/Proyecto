import csv
from faker import Faker
from datetime import datetime

class AlertTypesDataGenerator:
    def __init__(self, record_count, criticity_ids, category_ids):
        self.record_count = record_count
        self.criticity_ids = criticity_ids
        self.category_ids = category_ids
        self.fake = Faker()

    def generate_data(self):
        with open('csvs\AlertTypesEMPL.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Escribir los encabezados de las columnas
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
                    self.fake.random_element(self.criticity_ids),   # nCriticityID
                    self.fake.random_element(self.category_ids),    # nCategoryID
                    self.fake.user_name()[:20],                     # ID_Usuario
                    self.fake.bothify(text='??#')[:3],              # ID_Tipo_Documento
                    self.fake.user_name()[:20],                     # ID_Perfil_Supervisor
                    self.fake.unique.uuid4()[:50],                  # sGroupCustID
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),   # dtCreated
                    self.fake.date_time_this_century().strftime('%Y-%m-%d %H:%M:%S'),  # dtModified
                    self.fake.date_time_this_century().strftime('%Y-%m-%d %H:%M:%S')  # dtStatus
                ])

# Uso de la clase
record_count = 100  # Cantidad de registros a generar
criticity_ids = [i for i in range(1, 51)]  # Suponiendo que tenemos 50 IDs de criticity generados anteriormente
category_ids = [i for i in range(1, 51)]  # Suponiendo que tenemos 50 IDs de category generados anteriormente
generator = AlertTypesDataGenerator(record_count, criticity_ids, category_ids)
generator.generate_data()