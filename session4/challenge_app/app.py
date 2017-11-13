from flask import Flask, render_template, request, redirect, url_for

app = Flask("ChallengeApp")

# Dictionary to hold some data that will last between different requests
# during the user's visit to the app
session = {"bad_access": False, "message": ""}

@app.route("/")
def index():
    return render_template("index.html", bad_access=session["bad_access"],
                           message=session["message"])

@app.route("/home")
def home():
    user_info = request.values
    if user_info: # Check that you're not directly trying to access the page!
        # Check that you've typed in a name and a password...
        if user_info["name"] and user_info["password"]:
            update_session(bad_access=False, message="")
            return render_template("content.html")
        else:
            update_session(bad_access=True,
                           message="No username or password provided! Please try again!")
            # The url_for function takes the name of a function we've defined in this file,
            # and returns the relative URL to our application. The redirect function then
            # takes this URL and redirects the user to the page.
            return redirect(url_for("index"))
    else:
        update_session(bad_access=True,
                       message="You need to log in first before you can access the course content!")
        return redirect(url_for("index"))

def update_session(bad_access=False, message=""):
    session["bad_access"] = bad_access
    session["message"] = message

app.run(debug=True)
