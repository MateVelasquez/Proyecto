import pandas as pd
from sqlalchemy import create_engine
import traceback

class DataLoader:
    def __init__(self, host, port, user, password, database):
        self.database_uri = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        self.engine = None

    def connect_to_database(self):
        try:
            self.engine = create_engine(self.database_uri)
            print("Conexión a la base de datos establecida.")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            traceback.print_exc()

    def load_data_to_database(self, csv_file, table_name):
        try:
            if self.engine is not None:
                data = pd.read_csv(csv_file)
                data.to_sql(table_name, self.engine, if_exists='append', index=False)
                print(f"Datos de '{csv_file}' cargados exitosamente en '{table_name}'.")
            else:
                print("No hay conexión a la base de datos.")
        except Exception as e:
            print(f"Error al cargar datos de '{csv_file}' en la base de datos: {e}")
            traceback.print_exc()

# Uso de la clase
host = '10.10.10.2'
port = '3306'
user = 'dwh'
password = 'elcaro_4U'
database = 'BW_Business_Ware'

# Crear una instancia de la clase
loader = DataLoader(host, port, user, password, database)

# Conectar a la base de datos
loader.connect_to_database()

# Cargar los datos de todos los CSVs a sus respectivas tablas
csv_files_and_tables = {
    'csvs\customers.csv': 'tblCustomers',
    'csvs\AlertCases.csv': 'BW_TA_AlertCases',
    'csvs\caseCategory.csv': 'BW_TA_CaseCategories',
    'csvs\criticityLevel.csv': 'BW_TA_CriticityLevel',
    'csvs\AlertTypes.csv': 'BW_AlertTypes'
}

for csv_file, table_name in csv_files_and_tables.items():
    loader.load_data_to_database(csv_file, table_name)