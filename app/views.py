from os import popen
from flask import render_template
from app import app
from .requests import getMovies
@app.route("/")
def index():
    """
    view root page that returns the index page and its data
    """
    message = "Hello world"
    #movies
    popular_movies = getMovies("popular")
    upcoming_movie = getMovies("upcoming")
    get_showing_movies = getMovies("now_playing")

    print(popular_movies)
    title = "home - Welcome to the best movie review website online"
    return render_template("index.html", message = message, title = title, popular = popular_movies, upcoming = upcoming_movie, showing = get_showing_movies)


@app.route("/movie/<int:movie_id>")
def movie(movie_id):
    """
    view movie page that returns the movie details page and its data
    """
    return render_template("movie.html", id=movie_id)
