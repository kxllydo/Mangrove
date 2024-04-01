from flask import Flask, render_template, request
from datetime import datetime

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def list_of_users():
    username = request.form['username']
    return username

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/checklist/")
def checklist():
    return render_template("checklist.html")

@app.route("/classes/")
def classes():
    return render_template("classes.html")

@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/register/")
def register():
    return render_template("register.html")

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route("/calendar/")
def calendar():
    return render_template("calendar.html", events = webapp.events)

if __name__ == "__main__":
    app.run(debug=True)

# @app.route('/users', methods=['POST'])
# def list_of_users():
#     username = request.form['username']
#     return username

# @app.route("/")
# def home():
#     return render_template("home.html")

# @app.route("/about/")
# def about():
#     return render_template("about.html")

# @app.route("/checklist/")
# def checklist():
#     return render_template("checklist.html")

# @app.route("/classes/")
# def classes():
#     return render_template("classes.html")

# @app.route("/login/")
# def login():
#     return render_template("login.html")

# @app.route("/register/")
# def register():
#     return render_template("register.html")

# @app.route("/api/data")
# def get_data():
#     return app.send_static_file("data.json")

# @app.route("/calendar/")
# def calendar():
#     return render_template("calendar.html", events = webapp.events)

# if __name__ == "__main__":
#     app.run(debug=True)