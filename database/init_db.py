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
    tutor = Tutor(name="Tolosa", first_name="Jean", number="0123456789", mail="j.t@cgi.fr", enterprise=0)
    db.session.add(tutor)
    stage = Stage(title="Code un truc", date_start=datetime.now(), date_end=datetime.now(), resume="resume",
                  rapport="rapport", tutor=0, enterprise=0)
    db.session.add(stage)
    etudiant = Student(name="Riegel", first_name="Sam", nationality="French", birth_date=datetime.now(), taf1=0,
                       taf2=1, stage=0, promo=2024, occupation="Chef de projet")
    db.session.add(etudiant)
    etudiant2 = Student(name="Bailey", first_name="Laura", nationality="French", birth_date=datetime.now(), taf1=1,
                        taf2=0, stage=0, promo=2023, occupation="Developpeur")
    db.session.add(etudiant2)
    etudiant3 = Student(name="Mercer", first_name="Matthew", nationality="Américain", birth_date=datetime.now(), taf1=1,
                        taf2=0, stage=0, promo=2023, occupation="Developpeur")
    db.session.add(etudiant3)
    db.session.commit()