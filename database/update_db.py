from database.models import *
from datetime import datetime


def db_updateStudent(id, first_name, name, nationality, taf1, taf2, birth_date):
    print("db_updateStudent")
    student = User.query.get(id)
    student.first_name = first_name
    student.name = name
    student.nationality = nationality
    if birth_date != "":
        birth_date2 = datetime.strptime(birth_date,
                                        '%Y-%m-%d')
        student.birth_date = birth_date2
    student.taf1 = taf1
    student.taf2 = taf2

    db.session.commit()


def db_updateTaf(id, name, director):
    print("db_updateTaf")
    taf = Taf.query.get(id)
    taf.name = name
    taf.director = director
    db.session.commit()


def db_updateEnterprise(id, name):
    print("db_updateEnterprise")
    enterprise = Organisation.query.get(id)
    enterprise.name = name
    db.session.commit()


def db_updateOccupation(id, title, description, start_date, organisation):
    occupation = Occupation.query.get(id)
    occupation.title = title
    occupation.description = description
    if start_date != "":
        start_date2 = datetime.strptime(start_date, '%Y-%m-%d')
        occupation.start_date = start_date2
    occupation.organisation = organisation
    db.session.commit()


def db_updatePromo(id, annee):
    print("db_updatePromo")
    promo = Promo.query.get(id)
    promo.annee = annee
    db.session.commit()


def db_updateAccount(id, login, password, role, id_user):
    print("db_updateAccount")
    account = Account.query.get(id)
    account.login = login
    account.password = password
    account.role = role
    account.id_user = id_user
    db.session.commit()


def db_linkAccount(id, id_user):
    account = Account.query.get(id)
    account.id_user = id_user
    db.session.commit()
