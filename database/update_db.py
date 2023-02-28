from database.models import *
from datetime import datetime


def db_updateStudent(id, first_name, name, nationality, birth_date, taf1, taf2, stage, promo, occupation):
    print("db_updateStudent")
    student = Student.query.get(id)
    student.first_name = first_name
    student.name = name
    student.nationality = nationality
    student.birth_date = birth_date
    student.taf1 = taf1
    student.taf2 = taf2
    student.stage = stage
    student.promo = promo
    student.occupation = occupation
    db.session.commit()


def db_updateTaf(id, name, director):
    print("db_updateTaf")
    taf = Taf.query.get(id)
    taf.name = name
    taf.director = director
    db.session.commit()


def db_updateEnterprise(id, name):
    print("db_updateEnterprise")
    enterprise = Enterprise.query.get(id)
    enterprise.name = name
    db.session.commit()
