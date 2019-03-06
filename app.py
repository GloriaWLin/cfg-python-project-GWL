from flask import Flask, render_template, request

app = Flask(__name__) # create a new copy of a Flask app to work with

# decorate the function such that it can respond to request at the http address
# located before a funtion
# / = localhost:5000/
@app.route("/") 
def say_hello():
  # return "hello world!"
  return render_template("index.html") # update

# @app.route("/<name>") 
# def say_hello_to(name):
#   # return "hello world!"
#   return f"Hello {name} :)"

@app.route("/<name>")
def say_hello_to(name):
  return render_template("index.html", user=name)

@app.route("/feedback", methods=["POST"])
def get_feedback():
  # request.values is a dictionary holding any
  # POST request data that's not already part of the URL
  data = request.values

  return render_template("feedback.html", form_data=data)


app.run(debug=True) 
# starts up a web server controllable by Flask
# debug=True - automatically restart the program each time we made changes to our Python code