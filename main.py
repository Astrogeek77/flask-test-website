# import Flask class from flask module
from flask import Flask, render_template

app = Flask(__name__) # create Flask object
# print(__name__) ->  # __main__

# Response
# res = ""

# index route
@app.route("/")
def index():
    return render_template("home.html");


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True) # run flask app from within the main file