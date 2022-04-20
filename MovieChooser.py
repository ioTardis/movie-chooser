import json
import random
import os

exit_code = False
f = open('Movies.json') #import json file
data = json.load(f)

#choose a random movie from list
def random_movie(movie_list):
    random_index = random.randint(0, len(movie_list) - 1)
    print(f'''Your movie is {movie_list[random_index]["title"]}.
The director: {movie_list[random_index]["director"]}. 
Duration: {movie_list[random_index]["duration"]} minutes.
Actor: {movie_list[random_index]["actor"]}.
    ''')

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
        exit_code = True
    else:
        print('Not found\n')

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
        exit_code = True
    else:
        print('Not found\n')

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
        exit_code = True
    else:
        print('Not found\n')

if data != []:
    while not exit_code:
        print('''Welcome to the moviechooser!
1. Choose from the list
2. Choose from director
3. Choose from associated actor
4. Choose from time duration
        ''')

        match input('Input the option: '):
            case '1':
                random_index = random.randint(0, len(data['movies']) - 1)
                print(f'''Your movie is {data["movies"][random_index]["title"]}.
The director: {data["movies"][random_index]["director"]}. 
Duration: {data["movies"][random_index]["duration"]} minutes.
Actor: {data["movies"][random_index]["actor"]}.
                ''')
                exit_code = True
            case '2':
                director_movie(input('Insert director name: '))
            case '3':
                actor_movie(input('Insert actor name: '))
            case '4':
                duration_movie(int(input('Insert movie duration in minutes: ')))
    print('Have fun!')
    os.system("pause")
else:
    print('Error!Json file is empty')