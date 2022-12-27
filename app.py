from flask import Flask, render_template

# Create Flask Instance
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

fav_pizza = ["mushroom", "cheese", "chicken", 55]
@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name, pizzatopping=fav_pizza)


# Create Custom Errpr pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
