from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

# Basic Home page
@app.route("/")
def home():
    return "Hello to flask course page <h1>Start flask course!</h1>"

# Passing the pathvariables or input
@app.route("/<name>")
def home_page(name):
    return f"Welcome to homepage {name}"

# For redirection - this method routes /admin to home page
@app.route("/admin")
def admin():
    return redirect(url_for("home")) #include the function's name here

# Redirection 2
@app.route("/admin2")
def admin2():
    return redirect(url_for("home_page", name="Admin"))

# Including the html file
@app.route("/html")
def html_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()