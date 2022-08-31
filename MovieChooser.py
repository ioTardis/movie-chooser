import json
import random
import re

import PySimpleGUI as sg

f = open("Movies.json")  # import json file
data = json.load(f)

# choose a random movie


def random_from_list():
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


def director_movie(name):
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


def actor_movie(name):
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


def duration_movie(duration):
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


# check string input for only letters


def validate_text(input):
    letter_pattern = "[A-Za-z]"
    if re.match(letter_pattern, input):
        return True
    else:
        return False


# check number input for digits


def validate_number(input):
    number_pattern = "^\\d $"
    if re.match(number_pattern, input):
        return True
    else:
        return False


# add new movie to the json file


def add_movie(values):
    data["movies"].append(
        {
            "title": values["-TITLE-"],
            "actor": values["-ACTOR-"],
            "director": values["-DIRECTOR-"],
            "duration": values["-DURATION-"],
            "available": values["-AVAILABLE-"],
        }
    )
    with open("Movies.json", "w") as json_file:
        json.dump(data, json_file, indent=5)


def open_window():
    layout = [
        [sg.Text("Add a new movie into your list", key="add")],
        [sg.Text("*Title: "), sg.InputText("The Batman", key="-TITLE-")],
        [sg.Text("Director: "), sg.InputText("Matt Reeves", key="-DIRECTOR-")],
        [sg.Text("Actor: "), sg.InputText("Robert Pattinson", key="-ACTOR-")],
        [sg.Text("Duration: "), sg.InputText("176", key="-DURATION-")],
        [sg.Text("Available: "), sg.InputText("HBO", key="-AVAILABLE-")],
        [sg.Button("OK"), sg.Button("Exit")],
    ]
    window = sg.Window("Add movie", layout, modal=True)
    choice = None

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            if validate_text(values["-TITLE-"]):
                if validate_text(values["-DIRECTOR-"]):
                    if validate_text(values["-ACTOR-"]):
                        if validate_number(values["-DURATION-"]):
                            if validate_text(values["-AVAILABLE-"]):
                                add_movie(values)
                                sg.popup(
                                    "Movie added successfully in the list!",
                                    title="Success",
                                )
                                break
                            else:
                                sg.popup_error("Invalid input.Enter availability")
                        else:
                            sg.popup_error("Invalid input. Enter duration")
                    else:
                        sg.popup_error("Invalid input.Enter actor name")
                else:
                    sg.popup_error("Invalid input.Enter director name")
            else:
                sg.popup_error("Invalid input.Enter title")
    window.close()


sg.theme("DarkAmber")
if data != []:
    layout = [
        [sg.Text("")],
        [sg.Text("Welcome to the movie chooser! Choose the option:")],
        [sg.Button("From the list"), sg.Button("Choose director")],
        [sg.Button("From associated actor"), sg.Button("From time duration")],
        [sg.Button("Add new movie")],
        [sg.Button("Exit")],
        [sg.Text("")],
    ]

    window = sg.Window("Movie chooser", layout)
    while True:
        event, values = window.read()
        if (
            event == sg.WIN_CLOSED or event == "Exit"
        ):  # if user closes window or clicks cancel
            break
        elif event == "From the list":
            random_from_list()
        elif event == "Choose director":
            name = sg.popup_get_text("Enter the name:", title="Enter director")
            if validate_text(name):
                director_movie(name)
            else:
                sg.popup_error("Invalid input.Please, enter name")
        elif event == "From associated actor":
            name = sg.popup_get_text("Enter the name:", title="Enter actor")
            if validate_text(name):
                actor_movie(name)
            else:
                sg.popup_error("Invalid input. Please, enter name")
        elif event == "From time duration":
            time = sg.popup_get_text(
                "Enter duration time in minutes. E.g: 90:", title="Enter time"
            )
            if validate_number(time):
                duration_movie(int(time))
            else:
                sg.popup_error("Invalid input. Please, enter number")
        elif event == "Add new movie":
            open_window()
    window.close()
