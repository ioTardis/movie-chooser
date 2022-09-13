import json
import re

import PySimpleGUI as sg
from randomizing import *

## modal window to choose director


def choose_director(data):
    directors = map(
        lambda x: (data["movies"][x]["director"]),
range(len(data["movies"]))
    )
    layout = [
        [sg.Text("")],
        [
            sg.Listbox(
                values=list(dict.fromkeys(directors)),
                size=(40, 10),
                select_mode=sg.SELECT_MODE_SINGLE,
                enable_events=True,
                key="-DIRECTORLIST-"
            )
        ],
        [sg.Text("")],
        [sg.Button("OK"), sg.Button("Exit")],
    ]
    window = sg.Window("Choose director", layout, modal=True)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            director_movie(data, values["-DIRECTORLIST-"][0])
            break
    window.close()


## modal window to choose actor


def choose_actor(data):
    actors = []
    for index, element in enumerate(data["movies"]):
        if type(element["actor"]) == list:
            for index2, actor in enumerate(element["actor"]):
                actors.append(element["actor"][index2])
        else:
            actors.append(element["actor"])
    while "" in actors:
        actors.remove("")
    layout = [
        [sg.Text("")],
        [
            sg.Listbox(
                values=list(dict.fromkeys(actors)),
                size=(40, 10),
                select_mode=sg.SELECT_MODE_SINGLE,
                enable_events=True,
                key="-ACTORLIST-"
            )
        ],
        [sg.Text("")],
        [sg.Button("OK"), sg.Button("Exit")],
    ]
    window = sg.Window("Choose actor", layout, modal=True)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            actor_movie(data, values["-ACTORLIST-"][0])
            break
    window.close()


## dialog window to input new movie information


def add_movie_window(data):
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
                                add_movie(data, values)
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

# add new movie to the json file


def add_movie(data, values):
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


# check string input for only letters


def validate_text(input):
    letter_pattern = "[A-Za-z]"
    if re.match(letter_pattern, input):
        return True
    else:
        return False


# check number input for digits


def validate_number(input):
    if input.isdigit():
        return True
    else:
        return False