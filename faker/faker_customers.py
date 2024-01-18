# employee_data_generator.py (Reutilizado como customer_data_generator.py)
import csv
from faker import Faker
from datetime import datetime

class CustomerDataGenerator:
    def __init__(self, record_count):
        self.record_count = record_count
        self.fake = Faker()

    def generate_data(self):
        with open('csvs\customers.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                'sCustID', 'sCustName', 'sFirstName', 'sLastName', 'sMiddleName', 
                'sAddr1', 'sAddr2', 'sPlaceOfBirth', 'sCountryOfBirth', 
                'dtDateOfBirth', 'sPhone1', 'sEmail', 'sCity', 'sState', 
                'sCountry', 'sIndustryType', 'sOccupation', 'sEmployer', 
                'sBranchID', 'dtCreated', 'sCompanyAddress', 'sAcademicLevel', 'sLaborSituation'
            ])

            for _ in range(self.record_count):
                writer.writerow([
                    self.fake.unique.uuid4()[:50],  # sCustID
                    self.fake.name()[:200],         # sCustName
                    self.fake.first_name()[:50],    # sFirstName
                    self.fake.last_name()[:50],     # sLastName
                    self.fake.first_name()[:50],    # sMiddleName
                    self.fake.address()[:100],      # sAddr1
                    self.fake.address()[:100],      # sAddr2
                    self.fake.city()[:50],          # sPlaceOfBirth
                    self.fake.country()[:50],       # sCountryOfBirth
                    self.fake.date_of_birth().strftime('%Y-%m-%d %H:%M:%S'),  # dtDateOfBirth
                    self.fake.phone_number()[:50],  # sPhone1
                    self.fake.email()[:50],         # sEmail
                    self.fake.city()[:50],          # sCity
                    self.fake.state()[:50],         # sState
                    self.fake.country()[:50],       # sCountry
                    self.fake.job()[:200],          # sIndustryType
                    self.fake.job()[:200],          # sOccupation
                    self.fake.company()[:50],       # sEmployer
                    self.fake.unique.uuid4()[:250], # sBranchID
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # dtCreated
                    self.fake.address()[:100],      # sCompanyAddress
                    self.fake.word()[:50],          # sAcademicLevel
                    self.fake.word()[:50],          # sLaborSituation
                ])

# Uso de la clase
record_count = 100
generator = CustomerDataGenerator(record_count)
generator.generate_data()