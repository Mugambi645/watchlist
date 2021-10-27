from os import popen
from flask import render_template
from app import app
from .requests import getMovies, get_movie
@app.route("/")
def index():
    """
    view root page that returns the index page and its data
    """
    message = ""
    #movies
    popular_movies = getMovies("popular")
    upcoming_movie = getMovies("upcoming")
    get_showing_movies = getMovies("now_playing")

    print(popular_movies)
    title = "home - Welcome to the best movie review website online"
    return render_template("index.html", message = message, title = title, popular = popular_movies, upcoming = upcoming_movie, showing = get_showing_movies)


#movie details
@app.route("/movie/<int:id>")
def movie(id):
    """
    view function that returns movie id and its data
    """
    movie = get_movie(id)
    title = f"{movie.title}"
    return render_template("movie.html", title = title, movie = movie)
