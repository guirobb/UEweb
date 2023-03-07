from database.models import *
from datetime import datetime



#@app.route("/taf/<id>", methods=["DELETE"])
def db_deleteTaf(id) :
    print("db_deleteTaf")
    student = Taf.query.get(id)
    db.session.delete(student)
    db.session.commit()

#@app.route("/enterprise/<id>", methods=["DELETE"])
def db_deleteEnterprise(id) :
    print("db_deleteEnterprise")
    student = Enterprise.query.get(id)
    db.session.delete(student)
    db.session.commit()

def db_deleteStudent(id) :
    print("db_deleteStudent")
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()