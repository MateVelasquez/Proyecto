import traceback
from load.load_customers import CustomerDataLoader

try:
    # Configuración de la conexión y del archivo CSV
    host = '10.10.10.2'
    port = '3306'
    user = 'dwh'
    password = 'elcaro_4U'
    database = 'BW_Business_Ware'
    csv_file = './csvs/customers.csv'  # Asegúrate de que la ruta del archivo CSV sea correcta

    # Crear una instancia de la clase CustomerDataLoader
    loader = CustomerDataLoader(host, port, user, password, database, csv_file)

    # Conectar a la base de datos
    loader.connect_to_database()

    # Cargar los datos del CSV a la base de datos
    loader.load_data_to_database()

except Exception as e:
    print(f"Ha ocurrido un error: {e}")
    traceback.print_exc()