from flask import Flask, url_for, redirect, render_template, request

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

# Including the dynamic html file - JINJA
@app.route("/jinja/<name>")
def jinja_page(name):
    return render_template("jinja.html", content=name, names_list = ["Pravith", "Ranjith", "Bobby"])

# Template inheritance -> creating a skeleton in one file and using in others similar to OOPs
@app.route("/template-inheritance")
def template_inheritance():
    return render_template("template-inheritance.html")

# HTTP Methods
# HTTP considers the default method as GET
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")
    
@app.route("/<usr>")
def user(usr):
    return f"Hello {usr}!"

if __name__ == "__main__":
    app.run(debug=True) # debug=True makes the app reload automatically when changes are made to the code