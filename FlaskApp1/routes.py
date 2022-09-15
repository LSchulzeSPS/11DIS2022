from FlaskApp1 import app
from flask import render_template, request, json, Response, redirect, flash, url_for
from FlaskApp1.models import User, Course, Enrolment
from FlaskApp1.forms import RegisterForm, CalculatorForm, letterCountForm
# from FlaskApp1.calculator import addition, subtraction, multiplication, division

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
        if user and user.get_password(password):
            flash(f"{user.first_name}, you are successfully logged in!", "success")
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.", "danger")
    return render_template("login.html", form=form, title="Login", login=True)


@app.route("/courses")
@app.route("/courses/<term>")
def courses(term = None):
    if term is None:
        term = "Spring 2019"
    classes = Course.objects.order_by("courseID")
    return render_template("courses.html", courseData=classes, courses=True, term=term)
    # return render_template("courses.html", courses=True)


@app.route("/register", methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_id = User.objects.count()
        user_id += 1
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        flash("You are successfully registered!", "success")
        return redirect(url_for('index'))
    return render_template("register.html", title="Register", form=form, register=True)

@app.route("/calculator", methods=['GET'])

def calculator():
    form = CalculatorForm()
    num1 = form.num1.data
    num2 = form.num2.data
    if request.form.get('add'):
        result = num1 + num2
        operation = '+'
    elif request.form.get('min'):
        result = num1 - num2
        operation = '-'
    elif request.form.get('mul'):
        result = num1 * num2
        operation = '*'
    elif request.form.get('div'):
        result = num1 / num2
        operation = '/'
    elif request.form.get('mod'):
        result = num1 % num2
        operation = '%'
    return render_template("calculator.html", title="Calculator", form=form, calculator=True, calculation_success=True,
                           num1=num1, operation=operation, num2=num2, result=result)

@app.route("/calculatordf", methods=['GET'])
def calculatordf():
    return render_template("calculatordf.html")
@app.route("/operation_result/", methods=['POST'])
def operation_result():
    error = None
    result = None

    # request.form looks for:
    # html tags with matching "name= "
    first_input = request.form['Input1']
    second_input = request.form['Input2']
    operation = request.form['operation']

    try:
        input1 = float(first_input)
        input2 = float(second_input)

        # On default, the operation on webpage is addition
        if operation == "+":
            result = input1 + input2
        elif operation == "-":
            result = input1 - input2
        elif operation == "/":
            result = input1 / input2
        elif operation == "*":
            result = input1 * input2
        elif operation == "%":
            result = input1 % input2
        return render_template("calculatordf.html", input1=input1, input2=input2, operation=operation,
                               result=round(result,2), calculation_success=True)
    except ZeroDivisionError:
        return render_template("calculatordf.html", input1=input1, input2=input2, operation=operation,
                               result="Bad Input", calculation_success=False, error="You cannot divide by zero")

    except ValueError:
        return render_template("calculatordf.html", input1=input1, input2=input2, operation=operation,
                               result="Bad Input", calculation_success=False, error="Cannot perform numeric operations with provided input")

@app.route("/letterCount", methods=["GET", "POST"])
def letterCount():
    key = None
    form = letterCountForm()
    word = str(form.word.data).lower()
    my_dict = {}
    for letter in word:
        my_dict[letter] = my_dict.get(letter, 0) + 1
    tl = (f'There are {len(word)} total letters in the word {word}')
    tul = (f'There are {len(my_dict)} unique letters in the word {word}.')
    return render_template("letterCount.html", title="Letter Counter", form=form, letterCount=True, tl=tl, tul=tul, key=key, my_dict=my_dict)


@app.route("/enrolment", methods=["GET", "POST"])
# GET
def enrolment():
    courseID = request.form.get('courseID')
    courseTitle = request.form.get('title')
    if courseID:
        if Enrolment.objects(user_id=user_id, courseID=courseID):
            flash(f"Oops! You are already registered in this course {courseTitle}")
            return redirect(url_for("courses"))
        else:
            Enrolment(user_id=user_id,courseID=courseID)
            flash(f"You are enrolled in {courseTitle}!", "success")
    classes=None
    term = request.form.get('term')
    return render_template("enrolment.html", enrolment=True, title="Enrolment", classes=classes)
# POST
# def enrolment():
#     id = request.form['courseID']
#     title = request.form['title']
#     term = request.form['term']
#     return render_template("enrolment.html", enrolment=True, data={"id": id, "title": title, "term": term})


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
