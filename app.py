from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("layout.html.jinja2")


@app.route('/list/students')
def students():
    return render_template("listStudents.html.jinja2")

@app.route('/adm/edit/students')
def edit_students():
    return render_template("edituser.html.jinja2")


if __name__ == '__main__':
    app.run()
