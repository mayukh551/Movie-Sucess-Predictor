import requests as r
import os
# from imdb_Package import *
from Get_Actor_List import *
from Get_Movie_List import *

# c4779b30

# Fetching api keys from different websites

omdb_api_key = os.environ.get('OMDB_API')
tmdb_api_key = os.environ.get('MOVIE_API')
movie_name = input("Enter the movie name : ")
print('file-1')
# From OMDB website to fetch release year,
# all kinds of ratings,
# awards,
# cast and director and type

url = "http://www.omdbapi.com/?apikey=" + omdb_api_key + "&t=" + movie_name + "&plot=full"

response = r.get(url)
movie_data = response.json()

release_year = movie_data['Year']
print("Release Of Year", release_year)
director = movie_data['Director']
content_type = movie_data['Type']

#  Fetch List of all actors
cast_list = findCast(movie_name, release_year)
if cast_list == 0:
    print("Program Stopped!")
else:
    # if cast List not empty
    for actor in cast_list:
        main_code(actor)

    actor_avg_score = {}  # To save actor name along with its avg imdb rating of past 5 movies

    for i, j in actor_hist.items():
        score = []
        # i -> actor name
        # j -> movie name along with year in a dictionary
        for p, q in j.items():
            # Calling OMDB API to fetch imdb ratings
            # of last 5 movies of each actor
            url = "http://www.omdbapi.com/?apikey=" + omdb_api_key + "&t=" + str(p) + "&y=" + str(q) + "&plot=full"
            response = r.get(url)
            movie_data = response.json()
            if 'N' not in movie_data['imdbRating']:
                #  storing imdb score in a list
                score.append(float(movie_data['imdbRating']))
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
        print(f'{i} : %.2f' % j)

    # for i, j in director_avg_score.items():
    #     print(f'{i} : %.2f' % j)
