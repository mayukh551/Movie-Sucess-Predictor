import requests as r
import os
from imdb_Package import *
# from test_code import *

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
content_type = movie_data['Type']
# plot = movie_data['Plot']
# awards = movie_data['Awards']
# cast.append(director)
print(*cast)

#  CODE TO BE TESTED

# cast_list = findCast(movie_name)
# print(cast_list)
# cast = []
# for i in cast_list:
#     st = i
#     print(st, end=" ")
#     cast.append(st)
# print(cast)
# cast = cast[:3]
# print(cast)


# printing list of actors
for actor in cast:
    findMovies(actor)

# printing list of actors along with list of movies
# of each actor
actor_avg_score = {}
for i, j in actor_hist.items():
    score = []
    #  printing actor name
    print(i)
    # printing actor's movies list (p) along with release year (q)
    for p, q in j.items():
        print(p, ':', q)
        url = "http://www.omdbapi.com/?apikey=" + omdb_api_key + "&t=" + str(p) + "&y=" + str(q) + "&plot=full"
        response = r.get(url)
        movie_data = response.json()
        if 'N' not in movie_data['imdbRating']:
            score.append(float(movie_data['imdbRating']))
    print()
    # Find the average of best 3 movies
    score.sort()
    # Last 3 elements will be highest of all
    print(score)
    score_sum = sum(score[2:])
    avg = score_sum / 3
    print(f'Average rating of {i} : {avg}')
    actor_avg_score.setdefault(i, avg)
    print()

for i, j in actor_avg_score.items():
    print(i, ':', j)
