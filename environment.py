from flask import Flask, request, render_template

app = Flask(__name__)
app.debug=True

userDataBase = {
    "4a8g0105": "a8787",
    "stust": "university",
    "city": "tainan"
}

@app.route("/")
def index():
    return render_template("loginPage.html")

@app.route("/login", methods=['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if userDataBase[username] == password:
        return '<h1 id="login-result">Login Successed<h1>'
    else:
        return '<h1 id="login-result">Login Failed<h1>'

app.run()
