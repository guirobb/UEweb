
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
from database.models import *
import os
from database.database import init_database

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret_key1234"

#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db"
#db_path = os.path.join(os.path.dirname(__file__), 'database/database.db')
#db_uri = 'sqlite:///{}'.format(db_path)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///C:\\Users\\guill\\PycharmProjects\\flaskProject1\\database/database.db'

db.init_app(app)
with app.test_request_context(): # (2) bloc exécuté à l'initialisation de Flask
 init_database()


# @app.route("/clean")
def clean():
    db.create_all()
    db.drop_all()
    db.create_all()
    return "Cleaned!"

@app.route('/')
def index():
    print(clean())
    return render_template("layout.html.jinja2")

@app.route("/test")
def test():
    clean()
    student1 = Taf(name="Dassault", director="Pastor")
    db.session.add(student1)
    db.session.commit()
    sports = Taf.query.all()

    return render_template("index.html.jinja2", sports=sports)


if __name__ == '__main__':
    db = SQLAlchemy(app)
    app.run()
