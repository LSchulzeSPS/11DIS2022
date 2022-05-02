from FlaskApp1 import app
from flask import render_template, request, json, Response, redirect, flash
from FlaskApp1.models import User, Course, Enrolment
from FlaskApp1.forms import LoginForm, RegisterForm

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    # return "<h1>This is Boring</h1>"
    return render_template("index.html", index=True)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.objects(email=email).first()
        if user and password == user.password:
            flash(f"{user.first_name}, you are successfully logged in!", "success")
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.", "danger")
    return render_template("login.html", form=form, title="Login", login=True)


@app.route("/courses")
@app.route("/courses/<term>")
def courses(term='Spring 2022'):
    return render_template("courses.html", courseData=courseData, courses=True, term=term)
    # return render_template("courses.html", courses=True)


@app.route("/register")
def register():
    return render_template("register.html", register=True)


@app.route("/enrolment", methods=["GET", "POST"])
# GET
# def enrolment():
#     id = request.args.get('courseID')
#     title = request.args.get('title')
#     term = request.args.get('term')
#     return render_template("enrolment.html", enrolment=True, data={"id": id, "title": title, "term": term})
# POST
def enrolment():
    id = request.form['courseID']
    title = request.form['title']
    term = request.form['term']
    return render_template("enrolment.html", enrolment=True, data={"id": id, "title": title, "term": term})


@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if (idx == None):
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
    return Response(json.dumps(jdata), mimetype="application/json")


@app.route("/user")
def user():
    # User(user_id=1, first_name="Christian", last_name="Hur", email="christian@uta.com", password="abc1234").save()
    # User(user_id=2, first_name="Marry", last_name="Jane", email="mary.jane@uta.com", password="password123").save()
    users = User.objects.all()
    return render_template("user.html", user=users)
