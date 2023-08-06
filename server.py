from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "Keep it secret, keep it safe"


# our index route will handle rendering our form
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/users", methods=["POST"])
def create_user():
    print("Succesfully recieved POST info")
    print(request.form)
    name = request.form["name"]
    email = request.form["email"]
    return redirect("/show")


@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8007)
