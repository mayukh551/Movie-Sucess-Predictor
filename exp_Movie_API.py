import requests as r
import os
from imdb_Package import *
from GetActorsList import *

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
print("Release Of Year", release_year)
# cast = movie_data['Actors'].split(', ')
director = movie_data['Director']
content_type = movie_data['Type']
# print(*cast)

#  CODE TO BE TESTED
#  Fetch List of all actors
cast_list = findCast(movie_name, release_year)
if cast_list == 0:
    print("Program Stopped!")
else:
    # print('Cast : \n', *cast_list)
    # extracting only top five actors
    cast_list = cast_list[:5]
    # cast_list.append(director)
    # printing list of actors
    for actor in cast_list:
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

            # Calling OMDB API to fetch imdb ratings
            # of last 5 movies of each actor
            url = "http://www.omdbapi.com/?apikey=" + omdb_api_key + "&t=" + str(p) + "&y=" + str(q) + "&plot=full"
            response = r.get(url)
            movie_data = response.json()
            if 'N' not in movie_data['imdbRating']:
                #  storing imdb score in a list
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
        print(f'{i} : %.2f' % j)
