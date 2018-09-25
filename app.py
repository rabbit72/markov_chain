import markovify

from flask import Flask, render_template, request, redirect
from flask import jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import TextAreaField, validators


PATH_TO_DB = "./sqlite.db"

app = Flask(__name__)
app.secret_key = 'qwerty'
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{PATH_TO_DB}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models import Texts, Users
db.create_all()


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        text = request.form["text"]
        if 2 < len(text) < 50:
            text_model = markovify.Text(text)
            markov_sentence = text_model.make_sentence(tries=100)
            if markov_sentence:
                pass
        return redirect("/", code=302)


if __name__ == '__main__':
    app.run()
