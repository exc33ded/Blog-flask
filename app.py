from flask import Flask, render_template

# Create Flask Instance
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"

@app.route("/user/<name>")
def user(name):
    return f"<h2>Hello {name}</h2>"


if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
