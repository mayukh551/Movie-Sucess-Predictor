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
# plot = movie_data['Plot']
# awards = movie_data['Awards']
content_type = movie_data['Type']
# imdb_score = movie_data['imdbRating']

crew = cast.copy()
crew.extend(director)

print(*crew)
print()

# printing list of actors
for actor in cast:
    print(actor)
    print()
    findMovies(actor)
    print('\n')

# printing list of actors along with list of movies
# of each actor
score_sum = 0
actor_avg_score = {}
for i, j in actor_hist.items():
    #  printing actor name
    print(i)
    # printing actor's movies list (p) along with release year (q)
    for p, q in j.items():
        print(p, ':', q)
        url = "http://www.omdbapi.com/?apikey=" + omdb_api_key + "&t=" + p + "&y=" + str(q) + "&plot=full"
        response = r.get(url)
        movie_data = response.json()
        if movie_data['imdbRating'].isnumeric():
            score_sum = score_sum + movie_data['imdbRating']
    print()
    avg = score_sum // 5
    print(f'Average rating : {avg}')
    actor_avg_score.setdefault(i, avg)
    print()

for i, j in actor_avg_score.items():
    print(i, ':', j)
