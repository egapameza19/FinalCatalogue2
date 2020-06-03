from flask import Flask, render_template, request, url_for, redirect
import sqlite3

app = Flask(__name__,template_folder='Templates')

@app.route('/')
def hello() -> str:
    return render_template ('index.html')

@app.route('/home')
def home() -> str:
    return render_template ('index.html')

@app.route('/solid')
def solid() -> str:
    return render_template ('solid.html')

@app.route('/timeline')
def timeline() -> str:
    return render_template ('timeline.html')

@app.route('/training')
def training() -> str:
    return render_template ('training.html')

@app.route('/Publication')
def hello2() -> str:
    conn = sqlite3.connect('data_katalog.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Publikasi')
    rows = c.fetchall()
    print (c.fetchall()) 
    conn.commit()
    conn.close()

    xo = 24
    
    return render_template("Catalogue.html",rows = rows, xo=xo)

@app.route('/Details/<num>')
def hello3(num) -> int:
    conn = sqlite3.connect('data_katalog.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Publikasi where no = ?", (num,))
    rows = c.fetchall()
    print (c.fetchall()) 
    conn.commit()
    conn.close()

    return render_template ('Details.html', num=num , rows=rows)

@app.route('/list')
def list():
    conn = sqlite3.connect('data_katalog.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Publikasi')
    rows = c.fetchall()
    print (c.fetchall()) 
    conn.commit()
    conn.close()

    xo = 24
    
    return render_template("lala.html",rows = rows, xo=xo)

app.run(debug=True)