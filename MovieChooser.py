import json

import PySimpleGUI as sg
from dialogwindows import (
    add_movie_window,
    choose_actor_window,
    choose_director_window,
    edit_list_window,
    validate_number,
)
from randomizing import duration_movie, random_from_list

f = open("Movies.json")
data = json.load(f)


sg.theme("DarkAmber")
if data != []:
    layout = [
        [sg.Text("")],
        [sg.Text("Welcome to the movie chooser! Choose the option:")],
        [
            sg.Button("From the list", size=(20, 1)),
            sg.Button("Choose director", size=(20, 1)),
        ],
        [
            sg.Button("From associated actor", size=(20, 1)),
            sg.Button("From time duration", size=(20, 1)),
        ],
        [sg.Text("")],
        [
            sg.Button("Add new movie", size=(20, 1), button_color=("white", "#212121")),
            sg.Button("Edit list", size=(20, 1), button_color=("white", "#212121")),
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
            choose_director_window(data)
        elif event == "From associated actor":
            choose_actor_window(data)
        elif event == "From time duration":
            time = sg.popup_get_text(
                "Enter duration time in minutes. E.g: 90:", title="Enter time"
            )
            if validate_number(time):
                duration_movie(data, int(time))
            else:
                sg.popup_error("Invalid input. Please, enter number")
        elif event == "Add new movie":
            add_movie_window(data)
        elif event == "Edit list":
            edit_list_window(data)
    window.close()
