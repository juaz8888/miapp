from flask import Flask
from flask.templating import render_template


app=Flask(__name__)

@app.route("/")
def hola():
    return render_template("main.html",nombre="Juan Diaz")



app.run(port=5000,host="0.0.0.0",)

