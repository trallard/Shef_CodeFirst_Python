# To use functions from a library you installed via pip, you have to import them first.
# Importing functions using the "from x import a, b, c" style allows you to use
# the function directly as instead of having to write x.a(), x.b() etc each time.
from flask import Flask, render_template

# This creates the all important Flask application which will give us the ability
# to serve (respond) web pages back to our users based on the web address they
# typed in the browser
app = Flask("DemoApp")

# @app.route(...) is a "magic function" which supercharges a standard Python function
# to one which can handle requests from the user when they are visiting this route.  
@app.route("/")
def say_hello():
    return "Hello Code First Girls!"

# <name> is a placeholder which captures the value a user types after the /. For example,
# if "localhost:5000/darren" is being typed in the browser, "darren" will be captured in
# the `name` variable.
@app.route("/<name>")
def say_hello_to(name):
    """Example showing how to take URL parameter and capture its value."""
    return f"Hello {name}"

@app.route("/hello/<name>")
def show_hello_template(name):
    """Example showing to return and render an HTML template file back
    to the user's browser."""

    # By default, our templates do not know about variables such as `name` in
    # this case where we captured some value from the user with the web address (URL)
    # they typed in. So, to make use of such information, we need to pass this along
    # as additional variables after the name of the template in render_template(...).
    return render_template("hello.html", person=name)

# Passing in "debug=True" to app.run(...) will make your Flask powered server/
# application automatically refreshes upon any changes you make to this file.
app.run(debug=True)
