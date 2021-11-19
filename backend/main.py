import requests as r
import os
from imdb_Package import *
from movie_person_api import *
# from GetActorsList import *
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
    # extracting only top five actors
    cast_list = cast_list[:5]
    cast_list.append(director)
    print(*cast_list)
    # printing list of actors
    for person in cast_list:
        findMovies(person)
    print('\nfile-1\n')
    # printing list of actors along with list of movies
    # of each actor
    print(actor_hist)
    actor_avg_score = {}
    director_avg_score = {}
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
    print(director_hist)
    for i, j in director_hist.items():
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
        score_sum = score[-1] + score[-2] + score[-3]
        avg = score_sum / 3
        print(f'Average rating of {i} : {avg}')
        director_avg_score.setdefault(i, avg)
        print()

    for i, j in actor_avg_score.items():
        print(f'{i} : %.2f' % j)

    for i, j in director_avg_score.items():
        print(f'{i} : %.2f' % j)


