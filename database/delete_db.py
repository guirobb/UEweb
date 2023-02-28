from database.models import *
from datetime import datetime



#@app.route("/taf/<id>", methods=["DELETE"])
def db_deleteTaf() :
    print("db_deleteTaf")
    student = Taf.query.get(id)
    db.session.delete(student)
    db.session.commit()

#@app.route("/enterprise/<id>", methods=["DELETE"])
def db_deleteEnterprise() :
    print("db_deleteEnterprise")
    student = Enterprise.query.get(id)
    db.session.delete(student)
    db.session.commit()

def db_deleteStudent(id) :
    print("delete")
    print(id)
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()