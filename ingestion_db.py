import pandas as pd
import os
from sqlalchemy import create_engine
import logging

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s-%(levelname)s-%(message)s",
    filemode="a"
)

engine=create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    ''' This function will ingest the dataframe into database table '''
    df.to_sql(
        table_name,
        con=engine,
        if_exists='append',
        index=False,
        chunksize=100      
    )

def load_raw_data():
    ''' This function will load the CSVs as dataframe and insert into db '''
    for file in os.listdir('data'):
        if file.endswith('.csv'):
            logging.info(f'Ingesting {file} in db')
            print(f'Processing {file}...')

            try:
                for chunk in pd.read_csv('data/' + file, chunksize=50000):
                    ingest_db(chunk, file[:-4], engine)

                logging.info(f'{file} ingested successfully')

            except Exception as e:
                logging.error(f'Error in {file}: {e}')
                print(f'Error in {file}: {e}')

    logging.info('Ingestion Complete')
    print('Ingestion Complete')

if __name__=='__main__':
    load_raw_data()