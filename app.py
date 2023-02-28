from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql import func
from database.models import *
import os
from database.database import *
from database.init_db import *
from database.add_db import *
from database.delete_db import *
from database.update_db import *

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret_key1234"

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db"
# db_path = os.path.join(os.path.dirname(__file__), 'database/database.db')
# db_uri = 'sqlite:///{}'.format(db_path)
#app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///C:\\Users\\carlos\\Repos\\IMT2022\\WEB\\UEweb\\database/database.db'
app.config[
    "SQLALCHEMY_DATABASE_URI"] = 'sqlite:///C:\\Users\\guill\\PycharmProjects\\flaskProject1\\database/database.db'

db.init_app(app)
with app.test_request_context():  # (2) bloc exécuté à l'initialisation de Flask
    init_database()
    create_test_db()


# @app.route("/clean")
def clean():
    db.drop_all()
    db.create_all()
    return "Cleaned!"


@app.route('/')
def index():
    create_test_db()
    return render_template("layout.html.jinja2")


@app.route("/test")
def test():
    clean()
    # student1 = Taf(name="Dassault", director="Pastor")
    # db.session.add(student1)
    # db.session.commit()
    create_test_db()
    sports = Taf.query.all()

    return render_template("index.html.jinja2", sports=sports)


@app.route('/list/students')
def students():
    students = Student.query.all()
    print(students)
    return render_template("listStudents.html.jinja2", students=students)


@app.route('/list/students/edit')
def edit_students():
    ident = request.args.get('id', default='*', type=int)
    student = Student.query.filter(Student.id == ident)
    taf = Taf.query.all()
    print(student[0].birth_date)
    return render_template("edituser.html.jinja2", student=student, taf=taf)



@app.route('/promo')
def affiche_promo():
    print("coucou")
    promo = request.args.get('promo', default='*', type=int)
    print(promo)
    students = Student.query.filter(Student.promo == promo)
    return render_template("listStudents.html.jinja2", students=students)


@app.route('/stage')
def affiche_stage():
    print("coucou")
    promo = request.args.get('stage', default='*', type=int)
    print(promo)
    students = Student.query.filter(Student.stage == promo)
    return render_template("listStudents.html.jinja2", students=students)


@app.route('/taf')
def affiche_taf():
    promo = request.args.get('taf', default='*', type=str)
    print(promo)
    end = request.args.get('end', default='*', type=int)
    start = request.args.get('start', default='*', type=int)
    students = Student.query.filter(
        ((Student.taf1 == promo) & ((Student.promo - 1 <= end) & (Student.promo - 1 >= start))) | (
                (Student.taf2 == promo) & ((Student.promo <= end) & (Student.promo >= start))))
    return render_template("listStudents.html.jinja2", students=students)


if __name__ == '__main__':
    db = SQLAlchemy(app)
    app.run()




@app.route("/delete/student/", methods=["POST"])
def deleteStudent():
    id = request.form['id']
    db_deleteStudent(id)
    students = Student.query.all()
    print(students)
    return redirect("http://127.0.0.1:5000/list/students")


@app.route("/update/student", methods=["POST"])
def updateStudent():
    id = request.form['id']
    first_name = request.form['Input-firstname']
    name = request.form['Input-name']
    nationality = request.form['select-nationality']
    birth_date = request.form["Input-Date"]
    taf1 = request.form['select-TAF1']
    taf2 = request.form['select-TAF2']
    db_updateStudent(id, first_name, name, nationality, taf1, taf2, birth_date)
    return redirect("http://127.0.0.1:5000/list/students")

@app.route('/enterprise')
def search_enterprise():
    search_text = request.args.get('enterprise', default='*', type=str)
    print(search_text)
    enterprises = Enterprise.query.filter(Enterprise.name.ilike(f'%{search_text}%')).all()
    print(enterprises)
    return render_template("enterprise.html.jinja2", enterprises=enterprises)