from curses import window
import json
import random
import os
from this import s
from unicodedata import name
import PySimpleGUI as sg

f = open('Movies.json') #import json file
data = json.load(f)

#choose a random movie
def random_from_list():
    random_index = random.randint(0, len(data['movies']) - 1)
    sg.popup(f'''Your movie is {data["movies"][random_index]["title"]}
The director: {data["movies"][random_index]["director"]}
Duration: {data["movies"][random_index]["duration"]} minutes
Actor: {data["movies"][random_index]["actor"]}
Available on: {data["movies"][random_index]["available"]}
        ''', title='Your movie')

#function to choose movie from the given list
def random_movie(movie_list):
    random_index = random.randint(0, len(movie_list) - 1)
    sg.popup(f'''Your movie is {movie_list[random_index]["title"]}
The director: {movie_list[random_index]["director"]}
Duration: {movie_list[random_index]["duration"]} minutes
Actor: {movie_list[random_index]["actor"]}
Available on: {movie_list[random_index]["available"]}
        ''', title='Your movie')

#create a list of movies by a specific director
def director_movie(name):
    movies_list = []
    i = 0
    for movie in data['movies']:
        if data['movies'][i]['director'] == name:
            movies_list.append(data['movies'][i])
        i += 1
    if movies_list != []:
        random_movie(movies_list)
    else:
        sg.popup('There is no such a director in the list', title='Not found')

#create a list of movies by a specific actor
def actor_movie(name):
    movies_list = []
    i = 0
    for movie in data['movies']:
        if data['movies'][i]['actor'] == name:
            movies_list.append(data['movies'][i])
        for actor in data['movies'][i]['actor']:
            if actor == name:
                movies_list.append(data['movies'][i])
        i += 1
    if movies_list != []:
        random_movie(movies_list)
    else:
        sg.popup('There is no such an actor in the list', title='Not found')

#create a list of movies with certain duration
def duration_movie(duration):
    movies_list = []
    i = 0
    for movie in data['movies']:
        if data['movies'][i]['duration'] <= duration:
            movies_list.append(data['movies'][i])
        i += 1
    if movies_list != []:
        random_movie(movies_list)
    else:
        sg.popup('There is no such a movie with that duration time', title='Not found')

sg.theme('DarkAmber')
if data != []:
    layout = [  [sg.Text('')],
            [sg.Text('Welcome to the movie chooser! Choose the option:')],
            [sg.Button('From the list'), sg.Button('Choose director')],
            [sg.Button('From associated actor'), sg.Button('From time duration')],
            [sg.Button('Exit')],
            [sg.Text('')] ]
            
    window = sg.Window('Movie chooser', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
            break
        elif event == 'From the list':
            random_from_list()
        elif event == 'Choose director':
            name = sg.popup_get_text('Enter the name:', title='Enter director')
            director_movie(name)
        elif event == 'From associated actor':
            name = sg.popup_get_text('Enter the name:', title='Enter actor')
            actor_movie(name)
        elif event == 'From time duration':
            time = sg.popup_get_text('Enter duration time:', title='Enter time')
            duration_movie(int(time))
    window.close()