from database.models import *
from datetime import datetime


def db_addStudent(first_name, name, nationality, birth_date, taf1, taf2, stage, promo):
    birth_date2 = datetime.strptime(birth_date,
                                    '%Y-%m-%d')
    student = User(first_name=first_name, name=name, nationality=nationality, birth_date=birth_date2, taf1=taf1,
                   taf2=taf2,
                   stage=stage, promo=promo, role="user")
    print(student)
    db.session.add(student)
    print(db.session.commit())
    print("coucou")


def db_addTaf(name, director):
    print("db_addTaf")
    db.session.add(Taf(name=name, director=director))
    db.session.commit()


def db_addEnterprise(name):
    print("db_addEnterprise")
    db.session.add(Organisation(name=name))
    db.session.commit()


def db_addStage(title, date_start, date_end, resume, rapport, tutor, enterprise):
    date_start2 = datetime.strptime(date_start, '%Y-%m-%d')
    date_end2 = datetime.strptime(date_end, '%Y-%m-%d')
    db.session.add(
        Stage(title=title, date_start=date_start2, date_end=date_end2, resume=resume, rapport=rapport, tutor=tutor,
              enterprise=enterprise))
    db.session.commit()


def db_addTutor(name, first_name, number, mail, enterprise):
    db.session.add(
        Tutor(name=name, first_name=first_name, number=number, mail=mail, enterprise=enterprise)
    )
    db.session.commit()


def db_addOccupation(title, description, start_date, id_user, organisation):
    start_date2 = datetime.strptime(start_date, '%Y-%m-%d')
    db.session.add(Occupation(title=title, description=description, start_date=start_date2, id_user=id_user,
                              organisation=organisation))
    db.session.commit()