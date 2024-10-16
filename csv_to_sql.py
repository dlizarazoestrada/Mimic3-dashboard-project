import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

try:
    engine = create_engine('postgresql://admin:12345678@localhost/mimiciii')
    print("Connection to the database has been established.")
except SQLAlchemyError as e:
    print(f"The following error has ocurred: {e}")
    exit(1)

csv_files_path = os.path.join(os.getcwd(), 'mimic-iii-clinical-database-demo-1.4')
csv_files = [file for file in os.listdir(csv_files_path) if file.endswith('.csv')]


for csv_file in csv_files:
    try:
        df = pd.read_csv(os.path.join(csv_files_path,csv_file), encoding='latin1')
        
        table_name = os.path.splitext(csv_file)[0]
        
        df.to_sql(table_name, engine, index=False, if_exists='replace')
        
        print(f"Table '{table_name}' has been loaded to the database.")

    except FileNotFoundError as e:
        print(f"Error reading the file {csv_file}: {e}")
    except pd.errors.EmptyDataError as e:
        print(f"The file {csv_file} is empty: {e}")
    except pd.errors.ParserError as e:
        print(f"Error parsing the file {csv_file}: {e}")
    except SQLAlchemyError as e:
        print(f"Error loading the table '{table_name}' into the database: {e}")
    except Exception as e:
        print(f"An unexpected error occurred with the file {csv_file}: {e}")

print("All the tables has been loaded to the database.")