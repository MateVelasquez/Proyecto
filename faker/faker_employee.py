import csv
from faker import Faker
from datetime import datetime

class EmployeeDataGenerator:
    def __init__(self, record_count):
        self.record_count = record_count
        self.fake = Faker()

    def generate_data(self):
        with open('csvs\employee.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Escribir los encabezados de las columnas
            writer.writerow([
                'sEmploID', 'sEmployeeName', 'mMonthlyIncome', 'mTotalHeritage', 'sCity', 'sState',
                'sCountryofBirth', 'sBranch', 'dtOpened', 'dtDateofBirth', 'sAddress1', 'sStatus',
                'sOccupation', 'sMaritalStatus', 'nFamilyResponsibilities', 'sLegalSituation',
                'sDisability', 'nExperience', 'sHomePhone', 'sBusinessPhone', 'sAcademicLevel',
                'sEmail', 'sAddInfo1', 'fNumericInfo1', 'nVacation', 'dtCreated'
            ])

            for _ in range(self.record_count):
                writer.writerow([
                    self.fake.unique.uuid4()[:50],  # sEmploID
                    self.fake.name()[:200],         # sEmployeeName
                    round(self.fake.random_number(digits=5), 4),  # mMonthlyIncome
                    round(self.fake.random_number(digits=7), 4),  # mTotalHeritage
                    self.fake.city()[:30],          # sCity
                    self.fake.state()[:30],         # sState
                    self.fake.country()[:50],       # sCountryofBirth
                    self.fake.company()[:50],       # sBranch
                    self.fake.date_time_this_century().strftime('%Y-%m-%d %H:%M:%S'),  # dtOpened
                    self.fake.date_of_birth().strftime('%Y-%m-%d %H:%M:%S'),          # dtDateofBirth
                    self.fake.address()[:200],      # sAddress1
                    self.fake.word()[:20],          # sStatus
                    self.fake.job()[:200],          # sOccupation
                    self.fake.word()[:50],          # sMaritalStatus
                    self.fake.random_digit(),       # nFamilyResponsibilities
                    self.fake.word()[:20],          # sLegalSituation
                    self.fake.word()[:20],          # sDisability
                    self.fake.random_digit(),       # nExperience
                    self.fake.phone_number()[:50],  # sHomePhone
                    self.fake.phone_number()[:50],  # sBusinessPhone
                    self.fake.word()[:50],          # sAcademicLevel
                    self.fake.email()[:50],         # sEmail
                    self.fake.word()[:50],          # sAddInfo1
                    float(self.fake.random_number(digits=2)),  # fNumericInfo1
                    self.fake.random_int(min=0, max=30),        # nVacation
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # dtCreated
                ])

# Uso de la clase
record_count = 100  # Cantidad de registros a generar
generator = EmployeeDataGenerator(record_count)
generator.generate_data()