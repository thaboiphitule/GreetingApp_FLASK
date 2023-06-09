from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "admin"

@app.route('/')
def index():
    flash("what's your name")
    return render_template('index.html')

@app.route('/greet', methods=["POST", "GET"])
def greet():
    name = str(request.form['name_input'])
    flash("Hello " + name + ", great seeing you")
    return render_template('index.html')