from FlaskApp import app
from flask import render_template

#Website Building
@app.route('/')
@app.route('/index')
def index():
    print("called index")
    return render_template("index.html")
