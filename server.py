"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                    redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined                    

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
@app.route('/')
def homepage():
    """Home Page Route"""
    return render_template("homepage.html")

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""
    email = request.form.get("email")
    password= request.form.get("password")
    user = crud.create_user(email, password)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        crud.create_user(email, password)
        flash("Success! User has been created. Please log in.")
    return redirect("/")


@app.route('/movies')
def all_movies():
    """ View all movies"""
    movies = crud.get_all_movies()
    return render_template("all_movies.html", movies=movies)

@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """ Movie Details"""
    movie = crud.get_movie_by_id(movie_id)
    return render_template("movie_details.html", movie=movie)

@app.route('/movies/<movie_id>/ratings', methods = ["POST"])
def create_rating(movie_id):
    """ Movie Details"""
    rating = request.form.get('ratings')

    return render_template("movie_details.html", movie=movie)

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
