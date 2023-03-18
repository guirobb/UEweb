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

# from flask_cors import CORS


app = Flask(__name__)
# CORS(app)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret_key1234"

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db"
# db_path = os.path.join(os.path.dirname(__file__), 'database/database.db')
# db_uri = 'sqlite:///{}'.format(db_path)
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///C:\\Users\\carlos\\Repos\\IMT2022\\WEB\\UEweb\\database/database.db'
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


def list_all_students():
    return Student.query.all()


def list_all_tutors():
    return Tutor.query.all()


def list_all_companies():
    print(Organisation.query.all())
    return Organisation.query.all()


@app.route('/')
def index():
    create_test_db()
    return render_template("layout.html.jinja2")


@app.route('/login')
def login():
    accounts = Account.query.all()
    num = len(accounts)
    return render_template("login.html.jinja2", accounts=accounts, num=num)


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
    students = db.session.query(User, Promo, Stage).join(Promo, Stage).all()
    print(students)
    taf = Taf.query.all()
    num = len(students)
    promos = Promo.query.all()
    enterprises = Organisation.query.all()
    occupations= Occupation.query.join(User).filter(Occupation.active == 1).all()
    print(occupations)
    return render_template("listStudents.html.jinja2", students=students, taf=taf, filter=Filter(), num=num,
                           promos=promos, companies=enterprises, occupations=occupations)


@app.route('/list/students/edit')
def edit_students():
    ident = request.args.get('id', default='*', type=int)
    student = User.query.filter(User.id == ident)
    taf = Taf.query.all()
    return render_template("edituser.html.jinja2", student=student, taf=taf)


@app.route('/list/students/add')
def create_students():
    taf = Taf.query.all()
    stage = Stage.query.all()
    promo = Promo.query.all()
    return render_template("addStudent.html.jinja2", taf=taf, stages=stage, promos=promo)


@app.route('/list/occupation/add')
def create_job():
    ident = request.args.get('studentId', default='*', type=int)
    student = User.query.filter(User.id == ident)
    return render_template("addJob.html.jinja2", tutors=list_all_tutors(),
                           companies=list_all_companies(), students=student, ident=ident)


@app.route('/admin/taf/list')
def list_Taf():
    list_taf = Taf.query.all()
    return render_template("listTaf.html.jinja2", listTaf=list_taf)


@app.route('/admin/taf/edit')
def edit_taf():
    id_taf = request.args.get('id', default='*', type=int)
    taf = Taf.query.filter(Taf.id == id_taf)
    return render_template("editTaf.html.jinja2", taf=taf)


@app.route('/admin/companies/list')
def list_company():
    companies = Organisation.query.all()
    return render_template("listEnterprises.html.jinja2", companies=companies)


@app.route('/admin/company/edit')
def edit_company():
    id_company = request.args.get('id', default='*', type=int)
    enterp = Organisation.query.filter(Organisation.id == id_company)
    return render_template("editTaf.html.jinja2", company=enterp)


@app.route('/admin/promo/list')
def list_promos():
    promos = Promo.query.all()
    num = len(promos)
    return render_template("promotion.html.jinja2", promos=promos, num=num)


@app.route('/stage')
def affiche_stage():
    print("coucou")
    promo = request.args.get('stage', default='*', type=int)
    print(promo)
    students = User.query.filter(User.stage == promo)
    return render_template("listStudents.html.jinja2", students=students)


@app.route('/admin/internship/new')
def new_internship_form():
    ident = request.args.get('studentId', default='*', type=int)
    student = User.query.filter(User.id == ident)
    return render_template("addInternship.html.jinja2", tutors=list_all_tutors(),
                           companies=list_all_companies(), students=student, ident=ident)


@app.route('/taf')
def affiche_taf():
    promo = request.args.get('taf', default='*', type=str)
    print(promo)
    end = request.args.get('end', default='*', type=int)
    start = request.args.get('start', default='*', type=int)
    students = User.query.filter(
        ((User.taf1 == promo) & ((User.promo - 1 <= end) & (User.promo - 1 >= start))) | (
                (User.taf2 == promo) & ((User.promo <= end) & (User.promo >= start))))
    return render_template("listStudents.html.jinja2", students=students)


if __name__ == '__main__':
    db = SQLAlchemy(app)
    app.run()


@app.route("/delete/student/", methods=["POST"])
def deleteStudent():
    id = request.json['id']
    print(id)
    db_deleteStudent(id)
    return redirect("http://127.0.0.1:5000/list/students")


@app.route("/delete/enterprise/", methods=["POST"])
def deleteEnterprise():
    id = request.json['id']
    db_deleteEnterprise(id)
    return redirect("http://127.0.0.1:5000/list/students")


@app.route("/delete/taf/", methods=["POST"])
def deleteTaf():
    id = request.json['id']
    db_deleteTaf(id)
    return redirect("http://127.0.0.1:5000/list/students")


@app.route("/delete/promo/", methods=["POST"])
def deletePromo():
    id = request.json['id']
    db_deletePromo(id)
    return redirect("http://127.0.0.1:5000/list/students")

@app.route("/delete/occupation/", methods=["POST"])
def deleteJob():
    id = request.json['id']
    db_deleteOccupation(id)
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


@app.route("/update/enterprise", methods=["POST"])
def updateEnterprise():
    print("updateEnterprise")
    print(request.json)
    id = request.json['id']
    name = request.json['name']
    db_updateEnterprise(id, name, )
    return redirect("http://127.0.0.1:5000/admin/companies/list")


@app.route("/update/taf", methods=["POST"])
def updateTaf():
    id = request.json['id']
    name = request.json['name']
    director = request.json["responsable"]
    db_updateTaf(id, name, director)
    return redirect("http://127.0.0.1:5000/list/students")


@app.route("/update/promo", methods=["POST"])
def updatePromo():
    print("POST_Promo")
    id = request.json['id']
    annee = request.json['annee']
    db_updatePromo(id, annee)
    return redirect("http://127.0.0.1:5000/list/students")


@app.route('/enterprise')
def search_enterprise():
    search_text = request.args.get('enterprise', default='*', type=str)
    print(search_text)
    enterprises = Organisation.query.filter(Organisation.name.ilike(f'%{search_text}%')).all()
    print(enterprises)
    return render_template("enterprise.html.jinja2", enterprises=enterprises)


@app.route("/add/student", methods=["POST"])
def addStudent():
    print("accc")
    first_name = request.form['Input-firstname']
    name = request.form['Input-name']
    nationality = request.form['select-nationality']
    birth_date = request.form["Input-Date"]
    taf1 = request.form['select-TAF1']
    taf2 = request.form['select-TAF2']
    promo = request.form['select-Promo']
    account_id = request.form['id_user']
    db_addStudent(first_name, name, nationality, birth_date, taf1, taf2, 0, promo, " occupation")
    student = User.query.filter(User.first_name == first_name, User.name == name, User.taf1 == taf1, User.taf2 == taf2)
    db_linkAccount(account_id, student[0].id)
    return redirect("http://127.0.0.1:5000/admin/internship/new?studentId=" + str(student[0].id))


@app.route("/add/stage", methods=["POST"])
def addStage():
    title = request.form["Input-nameStage"]
    date_start = request.form["Input-date-start"]
    date_end = request.form["Input-date-end"]
    resume = request.form["Input-resumeStage"]
    rapport = request.form["Input-reportStage"]
    tutor = request.form["select-tutor"]
    enterprise = request.form["select-enterprise"]
    db_addStage(title, date_start, date_end, resume, rapport, tutor, enterprise)
    stage = Stage.query.all()
    student = User.query.all()
    student[len(student) - 1].stage = stage[len(stage) - 1].id
    db.session.commit()
    return redirect("http://127.0.0.1:5000/list/students")


@app.route("/add/occupation", methods=["POST"])
def addJob():
    title = request.form["Input-nameStage"]
    date_start = request.form["Input-date-start"]
    description = request.form["Input-resumeStage"]
    checked = request.form.getlist("checkbox")
    enterprise = request.form["select-enterprise"]
    student_id = request.form["id_user"]
    date_start2 = datetime.strptime(date_start, '%Y-%m-%d')
    print("checked : " , checked)
    if len(checked)>0:
        occupation = Occupation(title=title, start_date=date_start2, organisation=enterprise, id_user=student_id, active=1, description=description)
        db.session.add(occupation)
        db.session.commit()
    else:
        date_end = request.form["Input-date-end"]
        date_end2 = datetime.strptime(date_end, '%Y-%m-%d')
        occupation = Occupation(title=title, start_date=date_start2, end_date=date_end2, organisation=enterprise, id_user=student_id, active=0, description=description)
        db.session.add(occupation)
        db.session.commit()


    db.session.commit()
    return redirect("http://127.0.0.1:5000/list/students")


@app.route("/add/enterprise", methods=["POST"])
def addEnterprise():
    name = request.form['Input-name']
    db_addEnterprise(name)
    return redirect("http://127.0.0.1:5000/list/students")


@app.route("/add/taf", methods=["POST"])
def addTaf():
    name = request.form['Input-name']
    director = request.form["Input-Director"]
    db_updateTaf(name, director)
    return redirect("http://127.0.0.1:5000/list/students")


@app.route("/list/students/stage")
def research_internship():
    return redirect("http://127.0.0.1:5000/list/students")


@app.route("/detail/student")
def detailed_student():
    id = request.args.get('id', default='*', type=int)
    student = User.query.filter(User.id == id)[0]
    print(student.name)
    taf1 = Taf.query.filter(Taf.id == student.taf1)[0]
    taf2 = Taf.query.filter(Taf.id == student.taf2)[0]
    stage = Stage.query.filter(Stage.id == student.stage)[0]
    promo = Promo.query.filter(Promo.id == student.promo)[0]
    occupations = Occupation.query.filter(Occupation.id_user == student.id)
    return render_template("detailedStudent.html.jinja2", student=student, taf1=taf1, taf2=taf2, stage=stage,
                           promo=promo, occupations=occupations)


@app.route("/connection")
def checkCreation():
    users = User.query.all()
    test_presence = False
    i = 0
    j = -1
    id_user = request.args.get('id_user', default='*', type=int)
    id_account = request.args.get('id_account', default='*', type=int)
    print(users)
    print(len(users))
    while test_presence == False and i < len(users):
        print(users[i].id)
        print(id_user)
        if users[i].id == id_user:
            test_presence = True
            redirect("../")
            return render_template("layout.html.jinja2")
        else:
            i += 1
    if test_presence == False:
        redirect("../list/students/add")
        taf = Taf.query.all()
        stage = Stage.query.all()
        promo = Promo.query.all()
        return render_template("addStudent.html.jinja2", taf=taf, stages=stage, promos=promo, id_account=id_account)
