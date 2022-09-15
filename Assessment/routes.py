from Assessment import app
from flask import render_template, request
import random
from Assessment.forms import romanNumeralsForm, isomorphicPairForm

@app.route("/")
# @app.route("/romanNumerals", methods=['GET', 'POST'])
# def romanNumerals():
#     form=romanNumeralsForm
#     return render_template("romanNumerals.html", romanNumerals=True, form=form)
# @app.route("/complete/", methods=['GET', 'POST'])
# def complete():
#     return render_template("romanNumerals.html", romanNumerals=True, form=form)
#
# @app.route("/isomorphicPairs")
# def isomorphicPairs():
#     return render_template("isomorphicPairs.html", isomorphicPairs=True)

@app.route("/RPSLS", methods=['GET'])
def RPSLS():
    return render_template("RPSLS.html", RPSLS=True)
@app.route("/gameover/", methods=['POST'])
def gameover():
    order = ['rock', 'scissors', 'lizard', 'paper', 'spock']
    if request.form.get('rock'): player = 0
    elif request.form.get('paper'): player = 3
    elif request.form.get('scissors'): player = 1
    elif request.form.get('lizard'): player = 2
    elif request.form.get('spock'): player = 4
    opponent = random.randint(0, 4)

    if player == opponent: result = "drew with"
    elif player == 0 and opponent == 1 or player == 0 and opponent == 2: result = "beat"
    elif player == 1 and opponent == 2 or player == 1 and opponent == 3: result = "beat"
    elif player == 2 and opponent == 3 or player == 2 and opponent == 4: result = "beat"
    elif player == 3 and opponent == 4 or player == 3 and opponent == 0: result = "beat"
    elif player == 4 and opponent == 0 or player == 4 and opponent == 1: result = "beat"
    else: result = "lost to"

    return render_template("RPSLS.html", RPSLS=True, success=True, player=order[player],
                           opponent=order[opponent], result=result)

@app.route("/coffee", methods=["GET"])
def coffee():
    return render_template("coffee.html", coffee=True)
