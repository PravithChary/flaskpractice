from flask import Flask, url_for, redirect

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

if __name__ == "__main__":
    app.run()