
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql import func
from database.models import *
import os
from database.database import *

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
    #student1 = Taf(name="Dassault", director="Pastor")
    #db.session.add(student1)
    #db.session.commit()
    create_test_db()
    sports = Taf.query.all()

    return render_template("index.html.jinja2", sports=sports)


@app.route('/list/students')
def students():
    create_test_db()
    students = Student.query.all()
    print(students)
    return render_template("listStudents.html.jinja2", students=students)

@app.route('/adm/edit/students')
def edit_students():
    return render_template("edituser.html.jinja2")

@app.route('/promo')
def affiche_promo():
    print("coucou")
    create_test_db()
    promo = request.args.get('promo', default = '*', type = str)
    print(promo)
    students = Student.query.filter(Student.promo == promo)
    return render_template("listStudents.html.jinja2", students=students)


if __name__ == '__main__':
    db = SQLAlchemy(app)
    app.run()


def create_test_db():
    db.drop_all()
    db.create_all()
    taf1 = Taf(name="DCL", director="Théo CALVAR")
    db.session.add(taf1)
    taf2 = Taf(name="Login", director="Hélène COULON")
    db.session.add(taf2)
    enterprise = Enterprise(name="CGI")
    db.session.add(enterprise)
    tutor = Tutor(name="Tolosa", first_name="Jean", number="0123456789", mail="j.t@cgi.fr", enterprise=0)
    db.session.add(tutor)
    stage = Stage(title="Code un truc", date_start=datetime.now(), date_end=datetime.now(), resume="resume",
                  rapport="rapport", tutor=0, enterprise=0)
    db.session.add(stage)
    etudiant = Student(name="Pichereau", first_name="Hugo", nationality="French", birth_date=datetime.now(), taf1=0,
                       taf2=1, stage=0, promo="2024", occupation="Chef de projet")
    db.session.add(etudiant)
    etudiant2 = Student(name="Vigouroux", first_name="Laure", nationality="French", birth_date=datetime.now(), taf1=1,
                       taf2=0, stage=0, promo="2023", occupation="Developpeur")
    db.session.add(etudiant2)
    db.session.commit()