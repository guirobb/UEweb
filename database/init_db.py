from database.models import *
from datetime import datetime

def create_test_db():
    db.drop_all()
    db.create_all()
    taf1 = Taf(name="DCL", director="Théo CALVAR")
    db.session.add(taf1)
    taf2 = Taf(name="Login", director="Hélène COULON")
    db.session.add(taf2)
    enterprise = Enterprise(name="CGI")
    db.session.add(enterprise)
    enterprise2 = Enterprise(name="Cap Gemini")
    db.session.add(enterprise2)
    enterprise3 = Enterprise(name="EDF")
    db.session.add(enterprise3)
    promo = Promo(annee=2020)
    promo2 = Promo(annee=2021)
    db.session.add(promo)
    db.session.add(promo2)
    tutor = Tutor(name="Tolosa", first_name="Jean", number="0123456789", mail="j.t@cgi.fr", enterprise=0)
    db.session.add(tutor)
    stage = Stage(title="Code un truc", date_start=datetime.now(), date_end=datetime.now(), resume="resume",
                  rapport="rapport", tutor=0, enterprise=0)
    db.session.add(stage)
    stage2 = Stage(title="Code 2 truc", date_start=datetime.now(), date_end=datetime.now(), resume="resume",
                  rapport="rapport", tutor=0, enterprise=0)
    db.session.add(stage2)
    stage3 = Stage(title="Code 3 truc", date_start=datetime.now(), date_end=datetime.now(), resume="resume",
                   rapport="rapport", tutor=0, enterprise=0)
    db.session.add(stage3)
    etudiant = Student(name="Riegel", first_name="Sam", nationality="French", birth_date=datetime.now(), taf1=2,
                       taf2=1, stage=0, promo=1, occupation="Chef de projet")
    db.session.add(etudiant)
    etudiant2 = Student(name="Bailey", first_name="Laura", nationality="French", birth_date=datetime.now(), taf1=1,
                        taf2=2, stage=0, promo=1, occupation="Developpeur")
    db.session.add(etudiant2)
    etudiant3 = Student(name="Mercer", first_name="Matthew", nationality="Américain", birth_date=datetime.now(), taf1=1,
                        taf2=2, stage=0, promo=2, occupation="Developpeur")
    db.session.add(etudiant3)
    db.session.commit()