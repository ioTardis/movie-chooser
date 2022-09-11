import json
from msilib.schema import ListBox
import re

import PySimpleGUI as sg
from randomizing import *

f = open("Movies.json")  # import json file
data = json.load(f)


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


def choose_director():
    directors = map(lambda x: (data["movies"][x]["director"]), range(len(data["movies"])))
    layout = [
        [sg.Text("")],
        [sg.Listbox(values=list(dict.fromkeys(directors)), size=(40, 10), select_mode=sg.SELECT_MODE_SINGLE, enable_events=True)],
        [sg.Text("")],
        [sg.Text("Enter director"), sg.InputText(key="-DIRECTOR-")],
        [sg.Button("OK"), sg.Button("Exit")]
    ]
    window = sg.Window("Choose director", layout, modal=True)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            if validate_text(values["-DIRECTOR-"]):
                director_movie(data, values["-DIRECTOR-"])
                break
            else:
                sg.popup_error("Invalid input.Please, enter name")
    window.close()

sg.theme("DarkAmber")
if data != []:
    layout = [
        [sg.Text("")],
        [sg.Text("Welcome to the movie chooser! Choose the option:")],
        [
            sg.Button("From the list", size=(20, 1)), 
            sg.Button("Choose director", size=(20, 1))
        ],
        [
            sg.Button("From associated actor", size=(20, 1)), 
            sg.Button("From time duration", size=(20, 1))
        ],
        [sg.Text("")],
        [
            sg.Button("Add new movie", size=(20, 1), button_color=('white', '#212121')), 
            sg.Button("Edit list", size=(20, 1), button_color=('white', '#212121'))
        ],
        [sg.Text("")],
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
            random_from_list(data)
        elif event == "Choose director":
            choose_director()
        elif event == "From associated actor":
            name = sg.popup_get_text("Enter the name:", title="Enter actor")
            if validate_text(name):
                actor_movie(data, name)
            else:
                sg.popup_error("Invalid input. Please, enter name")
        elif event == "From time duration":
            time = sg.popup_get_text(
                "Enter duration time in minutes. E.g: 90:", title="Enter time"
            )
            if validate_number(time):
                duration_movie(data, int(time))
            else:
                sg.popup_error("Invalid input. Please, enter number")
        elif event == "Add new movie":
            open_window()
    window.close()
