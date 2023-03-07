from database.models import *
from datetime import datetime


def db_addStudent(first_name, name, nationality, birth_date, taf1, taf2, stage, promo, occupation):
    birth_date2 = datetime.strptime(birth_date,
                                   '%Y-%m-%d')
    db.session.add(
        Student(first_name=first_name, name=name, nationality=nationality, birth_date=birth_date2, taf1=taf1, taf2=taf2,
                stage=stage, promo=promo, occupation=occupation))
    db.session.commit()

def db_addTaf(name,director) :
    print("db_addTaf")
    db.session.add(Taf(name=name, director=director))
    db.session.commit()

def db_addEnterprise(name) :
    print("db_addEnterprise")
    db.session.add(Enterprise(name=name))
    db.session.commit()