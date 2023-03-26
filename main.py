# import Flask class from flask module
from flask import Flask, render_template, jsonify
# from modules.jobs import JOBS
from modules.database import load_jobs, load_job_from_db

app = Flask(__name__) # create Flask object
# print(__name__) ->  # __main__

JOBS = load_jobs()
# print(JOBS)

COMPANY_NAME = "INFOTECH"

# index route
@app.route("/")
def index():
    return render_template("home.html", jobs=JOBS, company_name=COMPANY_NAME);

# API for jobs
@app.route("/api/jobs")
def list_jobs():
  JOBS = load_jobs()
  return jsonify(JOBS)

# specific job page
@app.route("/job/<id>")
def show_job(id):
  id = int(id)
  job = load_job_from_db(id)
  # print(type(id))
  # print(id)
  # print(type(job))
  # print(job)
  
  if not job:
    return "Not Found", 404

  return render_template('jobpage.html',                          job=job, company_name = COMPANY_NAME)
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True) # run flask app from within the main file