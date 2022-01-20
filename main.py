from flask import Flask
import sqlite3
from flask.templating import render_template


app=Flask(__name__)

@app.route("/")
def hola():
    
    conn=sqlite3.connect("base.db")
    query="SELECT * FROM registro"
    cur=conn.cursor()

    cur.execute(query)

    dato=cur.fetchall()

    print(dato)

    return render_template("main.html",nombre=dato)


if __name__=='__main__':
    

    app.run(port=5000,host="0.0.0.0",debug=True)

