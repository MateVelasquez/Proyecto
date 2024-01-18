import csv
from faker import Faker
import random
import hashlib

class UsuarioDataGenerator:
    def __init__(self, record_count):
        self.record_count = record_count
        self.fake = Faker()

    def generate_data(self):
        with open('csvs\\usuario.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                'ID_Usuario', 'ID_Tipo_Documento', 'Licencia', 
                'Nombres_Usuario', 'Apellidos_Usuario', 'Nombre_Estado', 
                'User_Name', 'Password_Usuario', 'Email', 'Movil'
            ])

            for _ in range(self.record_count):
                # Generar un hash para simular un campo VARBINARY
                password = hashlib.sha256(self.fake.password().encode()).hexdigest()
                
                writer.writerow([
                    self.fake.bothify(text='??????????'),  # ID_Usuario
                    self.fake.bothify(text='###'),  # ID_Tipo_Documento
                    self.fake.bothify(text='??????????'),  # Licencia
                    self.fake.first_name(),  # Nombres_Usuario
                    self.fake.last_name(),  # Apellidos_Usuario
                    self.fake.word(),  # Nombre_Estado
                    self.fake.user_name(),  # User_Name
                    password,  # Password_Usuario
                    self.fake.email(),  # Email
                    self.fake.phone_number()  # Movil
                ])

# Ejemplo de uso
record_count = 100  # Cantidad de registros a generar
generator = UsuarioDataGenerator(record_count)
generator.generate_data()