from database.database import db


class Enterprise(db.Model):
    __tablename__ = "Enterprise"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)


class Taf(db.Model):
    __tablename__ = "Taf"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    director = db.Column(db.Text)


class Tutor(db.Model):
    __tablename__ = "Tutor"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    first_name = db.Column(db.Text)
    number = db.Column(db.Integer)
    mail = db.Column(db.Text)
    enterprise = db.Column(db.Integer, db.ForeignKey('Enterprise.id'))


class Stage(db.Model):
    __tablename__ = "Stage"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    date_start = db.Column(db.DateTime)
    date_end = db.Column(db.DateTime)
    resume = db.Column(db.Text)
    rapport = db.Column(db.Text)
    tutor = db.Column(db.Integer, db.ForeignKey('Tutor.id'))
    enterprise = db.Column(db.Integer, db.ForeignKey('Enterprise.id'))

class Promo(db.Model):
    __tablename__ = "Promo"
    id = db.Column(db.Integer, primary_key=True)
    annee = db.Column(db.Integer)

class Student(db.Model):
    __tablename__ = "Student"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    first_name = db.Column(db.Text)
    nationality = db.Column(db.Text)
    birth_date = db.Column(db.DateTime)
    taf1 = db.Column(db.Integer, db.ForeignKey('Taf.id'))
    taf2 = db.Column(db.Integer, db.ForeignKey('Taf.id'))
    stage = db.Column(db.Integer, db.ForeignKey('Stage.id'))
    promo = db.Column(db.Integer, db.ForeignKey('Promo.id'))
    occupation= db.Column(db.Text)

