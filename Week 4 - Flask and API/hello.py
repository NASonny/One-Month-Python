# For flask you can install in with pip install flask 
# Also to start the website you will need to use  [ $env:FLASK_APP="hello" ] and just after use "python -m flask run"
# "python -m flask run --debug" for having a realtime change and not the necessary to reboot the server

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    title = "Homepage"
    return render_template("index.html", title=title)

@app.route("/about")
def about():
    title = "About"
    return render_template("about.html",title=title)

@app.route("/contact")
def contact():
    title = "Contact"
    return render_template("contact.html", title=title)