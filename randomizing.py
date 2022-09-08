import random
import PySimpleGUI as sg

# choose a random movie

def random_from_list(data):
    random_index = random.randint(0, len(data["movies"]) - 1)
    sg.popup(
        f"""Your movie is {data["movies"][random_index]["title"]}
The director: {data["movies"][random_index]["director"]}
Duration: {data["movies"][random_index]["duration"]} minutes
Actor: {data["movies"][random_index]["actor"]}
Available on: {data["movies"][random_index]["available"]}
        """,
        title="Your movie",
    )

# function to choose movie from the given list


def random_movie(movie_list):
    random_index = random.randint(0, len(movie_list) - 1)
    sg.popup(
        f"""Your movie is {movie_list[random_index]["title"]}
The director: {movie_list[random_index]["director"]}
Duration: {movie_list[random_index]["duration"]} minutes
Actor: {movie_list[random_index]["actor"]}
Available on: {movie_list[random_index]["available"]}
        """,
        title="Your movie",
    )

# create a list of movies by a specific director


def director_movie(data, name):
    movies_list = []
    i = 0
    for movie in data["movies"]:
        if data["movies"][i]["director"] == name:
            movies_list.append(data["movies"][i])
        i = 1
    if movies_list != []:
        random_movie(movies_list)
    else:
        sg.popup("Cannot find a director in the list", title="Not found")


# create a list of movies by a specific actor


def actor_movie(data, name):
    movies_list = []
    i = 0
    for movie in data["movies"]:
        if data["movies"][i]["actor"] == name:
            movies_list.append(data["movies"][i])
        for actor in data["movies"][i]["actor"]:
            if actor == name:
                movies_list.append(data["movies"][i])
        i = 1
    if movies_list != []:
        random_movie(movies_list)
    else:
        sg.popup("Cannot find an actor in the list", title="Not found")


# create a list of movies with certain duration


def duration_movie(data, duration):
    movies_list = []
    i = 0
    for movie in data["movies"]:
        if data["movies"][i]["duration"] <= duration:
            movies_list.append(data["movies"][i])
        i = 1
    if movies_list != []:
        random_movie(movies_list)
    else:
        sg.popup("Cannot find a movie with that duration", title="Not found")

