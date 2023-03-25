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