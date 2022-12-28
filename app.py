from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Create Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "qwerty2212"

# Create a form class
class NamerForm(FlaskForm):
    name = StringField("What's your Name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route("/")
def index():
    return render_template("index.html")

fav_pizza = ["mushroom", "cheese", "chicken", 55]
@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name, pizzatopping=fav_pizza)


# Create Custom Error pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

# Create Name Page
@app.route("/name", methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name=form.name.data
        form.name.data = ''
    return render_template("name.html",name=name, form=form)


if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
