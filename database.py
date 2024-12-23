from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os


load_dotenv()

# it fetch credentials from .env file
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')


database_url = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(database_url)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text('select * from jobs'))
        columns = result.keys()
        jobs = []
        for row in result:
            jobs.append(dict(zip(columns, row)))
    return jobs


        

   
