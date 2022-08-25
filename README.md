# movie-chooser

:clapper: simple program that helps to finally choose a movie from a list for the evening.  
Console program written in Python that interacts with list of movies in json formatted external file.
Graphical interface is created using PySimpleGUI

## Features

- Choose a movie from the predefined list
- Choose a movie by specific director
- Choose a movie by specific actor
- Choose a movie of a certain duration
- Show which streaming service have it

## Ideas for future development

- Possibility to edit list in the program
- Change the format of a storage
- Retrieve data about movie with API and don't store it locally
- Display a clickable link to get to the movie
- Update searching system. Case insensitive, only with name or surname
- Add a feature to change the list file

### List format
```
{
	"movies": [
	{
		"title": "Movie title",
		"actor": "Famous Actor",
		"director": "Best Director",
		"duration": 100,
		"available": "Netflix"
	}
]}
```
