from os import popen
from flask import render_template,request,redirect,url_for
from app import app
from .requests import getMovies, get_movie,search_movie
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
    title = "home - Welcome to the best movie review website online"
    search_movie = request.args.get("movie_query")
    if search_movie:
        return redirect(url_for("search", movie_name = search_movie))
    else:
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


#search movie function
@app.route("/search/<movie_name>")
def search(movie_name):
    """
    View function to display the search results
    """
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f" search results for {movie_name}"
    return render_template("search.html", movies=searched_movies)


