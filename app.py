from flask import Flask, render_template

app = Flask(__name__) # create a new copy of a Flask app to work with

# decorate the function such that it can respond to request at the http address
# located before a funtion
# / = localhost:5000/
@app.route("/") 
def say_hello():
  # return "hello world!"
  return render_template("index.html") # update

app.run(debug=True) 
# starts up a web server controllable by Flask
# debug=True - automatically restart the program each time we made changes to our Python code