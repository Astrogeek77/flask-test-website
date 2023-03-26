import os
from sqlalchemy import create_engine, text

USERNAME = os.environ['username']
PASSWORD = os.environ['password']
HOST = os.environ['host']
DATABASE = os.environ['database']

DB_CONN_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}?charset=utf8mb4"
CONN_ARGS = {
        "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
}
engine = create_engine(DB_CONN_URL, connect_args=CONN_ARGS)

def load_jobs():
  jobs = []
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
  
    # convert from sql legacy tpe to a dict 
    for result_row in result.all():
      jobs.append(result_row._mapping)
  
  return jobs

# print(load_jobs())

def load_job_from_db(id):
  id = int(id)
  with engine.connect() as conn:
    result = conn.execute(
       text(f"SELECT * FROM jobs WHERE id={id}")
      )
    rows = []
    for row in result.all():
      rows.append(row._mapping)
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])
# print(type(load_job_from_db("2")))      
# print(load_job_from_db("2"))      

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
      f"INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES ({job_id}, {data['full_name']}, {data['email']}, {data['linkedin_url']}, {data['education']}, {data['work_experience']}, {data['resume_url']})")
    
    conn.execute(query)

    