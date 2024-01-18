import pandas as pd
from sqlalchemy import create_engine
import traceback

class EmployeeDataLoader:
    def __init__(self, host, port, user, password, database, csv_file, table_name):
        self.database_uri = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        self.csv_file = csv_file
        self.table_name = table_name
        self.engine = None

    def connect_to_database(self):
        try:
            self.engine = create_engine(self.database_uri)
            print("Conexión a la base de datos establecida.")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            traceback.print_exc()

    def load_data_to_database(self):
        try:
            if self.engine is not None:
                data = pd.read_csv(self.csv_file)
                data.to_sql(self.table_name, self.engine, if_exists='append', index=False)
                print("Datos cargados exitosamente en la base de datos.")
            else:
                print("No hay conexión a la base de datos.")
        except Exception as e:
            print(f"Error al cargar datos en la base de datos: {e}")
            traceback.print_exc()

# Uso de la clase
host = '10.10.10.2'
port = '3306'
user = 'dwh'
password = 'elcaro_4U'
database = 'BW_Business_Ware'
csv_file = 'csvs\employee.csv'  # Nombre del archivo CSV generado
table_name = 'tblEmployees'  # Nombre de la tabla en la base de datos

# Crear una instancia de la clase
loader = EmployeeDataLoader(host, port, user, password, database, csv_file, table_name)

# Conectar a la base de datos
loader.connect_to_database()

# Cargar los datos del CSV a la base de datos
loader.load_data_to_database()