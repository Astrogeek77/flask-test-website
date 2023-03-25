# import Flask class from flask module
from flask import Flask, render_template, jsonify
# from modules.jobs import JOBS
from modules.database import load_jobs

app = Flask(__name__) # create Flask object
# print(__name__) ->  # __main__

JOBS = load_jobs()
print(JOBS)

# index route
@app.route("/")
def index():
    return render_template("home.html", jobs=JOBS, company_name="Jester");

# API for jobs
# @app.route("/api/jobs")
# def list_jobs():
#   return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True) # run flask app from within the main file