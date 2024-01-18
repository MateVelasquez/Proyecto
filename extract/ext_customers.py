import traceback
from util.db_connection import Db_Connection
import pandas as pd

def extraer_customers ():

    try:
        filename = './csvs/customers.csv'
        customers = pd.read_csv(filename)
        return customers

    except:
        traceback.print_exc()
    finally:
        pass
