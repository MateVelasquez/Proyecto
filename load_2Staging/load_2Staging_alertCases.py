import pandas as pd
from sqlalchemy import create_engine
import traceback

class AlertCaseDataLoader:
    def __init__(self, source_db_info, target_db_info, sql_query, table_name):
        self.source_engine = self.create_engine(source_db_info)
        self.target_engine = self.create_engine(target_db_info)
        self.sql_query = sql_query
        self.table_name = table_name

    def create_engine(self, db_info):
        uri = f"mysql+pymysql://{db_info['user']}:{db_info['password']}@{db_info['host']}:{db_info['port']}/{db_info['database']}"
        return create_engine(uri)

    def load_data_to_database(self):
        try:
            data = pd.read_sql(self.sql_query, self.source_engine)
            data.to_sql(self.table_name, self.target_engine, if_exists='append', index=False)
            print("Datos cargados exitosamente en la base de datos.")
        except Exception as e:
            print(f"Error al cargar datos en la base de datos: {e}")
            traceback.print_exc()

# Información de la base de datos de origen
source_db_info = {
    'host': '10.10.10.2',
    'port': '3306',
    'user': 'dwh',
    'password': 'elcaro_4U',
    'database': 'BW_Business_Ware'
}

# Información de la base de datos de destino
target_db_info = {
    'host': '10.10.10.2',
    'port': '3306',
    'user': 'dwh',
    'password': 'elcaro_4U',
    'database': 'staging'
}

# Crear una instancia de la clase
sql_query = "SELECT * FROM BW_TA_AlertCases"
table_name = 'BW_TA_AlertCases'
loader = AlertCaseDataLoader(source_db_info, target_db_info, sql_query, table_name)

# Cargar los datos del SQL a la base de datos
loader.load_data_to_database()