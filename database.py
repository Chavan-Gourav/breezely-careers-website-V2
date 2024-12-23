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


#loads job id from database
def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text('SELECT * FROM jobs WHERE id = :val'),
            {"val": id}
        )
        columns = result.keys()  
        rows = result.all()  
        if len(rows) == 0:
            return None
        else:
            return dict(zip(columns, rows[0]))  



def add_application_to_db(job_id, data):
    try:
        with engine.connect() as conn:
            query = text('INSERT INTO applications (job_id, full_name, email, linkedin_url, resume_url) '
                         'VALUES (:job_id, :full_name, :email, :linkedin_url, :resume_url)')
            
            # Pass parameters as a dictionary
            conn.execute(query, {
                'job_id': job_id,
                'full_name': data['full_name'],
                'email': data['email'],
                'linkedin_url': data['linkedin_url'],
                'resume_url': data['resume']
            })
            
    
            conn.commit()

    except Exception as e:
        print(f"Error occurred while inserting application: {e}")
        

        

   
