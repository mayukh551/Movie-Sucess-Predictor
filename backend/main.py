import requests as r
import os
from imdb_Package import *

# c4779b30

# Fetching api keys from different websites

omdb_api_key = os.environ.get('OMDB_API')
tmdb_api_key = os.environ.get('MOVIE_API')
movie_name = input("Enter the movie name : ")

# From OMDB website to fetch release year,
# all kinds of ratings,
# awards,
# cast adn director and type

url = "http://www.omdbapi.com/?apikey=" + omdb_api_key + "&t=" + movie_name + "&plot=full"

response = r.get(url)
movie_data = response.json()

release_year = movie_data['Year']
cast = movie_data['Actors'].split(', ')
director = movie_data['Director']
plot = movie_data['Plot']
awards = movie_data['Awards']
content_type = movie_data['Type']
ratings = movie_data['Ratings']

crew = cast.copy()
crew.extend(director)

print(*cast)
print()

# printing list of actors
for actor in cast:
    print(actor)
    print()
    findMovies(actor)
    print('\n')

# printing list of actors along with list of movies
# of each actor
for i, j in actor_hist.items():
    #  printing actor name
    print(i)
    # printing actor's movies list (p) along with release year (q)
    for p, q in j.items():
        print(p, ':', q)
    print()

# hi there
