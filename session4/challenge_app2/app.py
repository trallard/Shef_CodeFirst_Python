from flask import Flask, render_template, request

app = Flask("ChallengeApp2")

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/", methods=["POST"])
def gather_feedback():
    antidote = request.form["antidote"]
    
    # How would you modify this to fix the corrupted app?
    return render_template("hello.html")

# "debug=True" causes Flask to automatically refresh upon any changes you
# make to this file.
app.run(debug=True)
