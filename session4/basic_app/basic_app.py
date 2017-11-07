from flask import Flask, render_template, request

app = Flask("BasicDemoApp")

@app.route("/")
def index():
    """Example showing how to return a string back to the user's browser
    when they visit the root path of the website."""

    return render_template("index.html", title="Home page")

@app.route("/feedback")
def gather_feedback():
    """Example showing how to retrieve data from requests."""

    # a neat way for accessing data from both GET and POST requests!
    data = request.values

    # We can have a peek at what the data looks like in the console if we
    # print the result we got from the user
    print(f"Name submitted was: {data['name']}")
    print(f"Email submitted was: {data['email']}")
    return render_template("feedback.html", form_data=data, title="Feedback response")

@app.route("/feedback", methods=["POST"])
def gather_post_feedback():
    """Example showing how to handle write a function to handle POST requests."""

    return gather_feedback()

@app.route("/get_feedback", methods=["GET", "POST"])
def multi_method_gather_feedback():
    """Example showing how to write a function handling both GET and POST#
    requests at the same time."""

    return gather_feedback()

# More generic routes (i.e ones in angled brackets) should be placed nearer
# the bottom of the code to act as fallback, as the order in which the
# routes are defined matters. Try putting this above the `gather_feedback` function
# and see what happens!
@app.route("/<name>")
def say_hello_to(name):
    """Example showing how to take URL parameter and capture its value, as
    well as how to return a string back to the user's browser."""

    return f"Hello {name}"

@app.route("/hello/<name>")
def show_hello_template(name):
    """Example showing to return and render an HTML template file back
    to the user's browser."""

    return render_template("hello.html", person=name, title="Greetings")

# "debug=True" causes Flask to automatically refresh upon any changes you
# make to this file.
app.run(debug=True)
