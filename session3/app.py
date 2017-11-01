from flask import Flask, render_template

app = Flask("DemoApp")

@app.route("/")
def say_hello():
    return "Hello Code First Girls!"

@app.route("/<name>")
def say_hello_to(name):
    """Example showing how to take URL parameter and capture its value"""
    return f"Hello {name}"

@app.route("/hello/<name>")
def show_hello_template(name):
    return render_template("hello.html", name=name)

app.run(debug=True)
