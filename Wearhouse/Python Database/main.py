from flask import Flask, render_template, redirect, url_for , request
import flask_sqlalchemy
import sqlite3

# db = sqlite3.connect("computer-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE computers (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO computers VALUES(0, 'Dell Vostro', 'Dell', '9.3')")
# db.commit()

app = Flask(__name__)

pc_list = []

@app.route("/")
def home():
    return render_template("index.html" , pc_list = pc_list)

@app.route("/add" , methods=["GET", "POST"])
def add(): 
    if request.method == "POST":
        data = request.form
        new_book = {
            "title": data["title"],
            "author": data["author"],
            "rating": data["rating"]
        }
        pc_list.append(new_book)
        return render_template("index.html" , pc_list = pc_list)
    return render_template("add.html")

if __name__ == '__main__':
    app.run(debug=True)