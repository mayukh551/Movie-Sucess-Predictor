import requests as r
import os
from Get_Actor_List import *
from Get_Movie_List import *
from Director_Movies_Score import *


# c4779b30


def extract_best_movies(ratings):
    s = 0
    average = 0.0
    no_of_scores = len(ratings)
    # s is score out of 10
    # So is average
    if no_of_scores >= 4:
        s = ratings[-1] + ratings[-2] + ratings[-3]
        average = s / 3
    elif no_of_scores == 3:
        s = sum(ratings[1:])
        average = s / 2
    elif no_of_scores == 2:
        average = sum(ratings) / 2
    elif no_of_scores == 1:
        average = sum(ratings)
    return average


# Fetching api keys from different websites

omdb_api_key = os.environ.get('OMDB_API')
tmdb_api_key = os.environ.get('MOVIE_API')

# From OMDB website to fetch release year,
# all kinds of ratings,
# awards,
# cast and director and type
# + omdb_api_key +

movie_name = input("Enter the movie name : ")
y = input("Enter the release year: ")
print('file-1')

url = "http://www.omdbapi.com/?apikey=c4779b30&t=" + movie_name + "&y=" + y + "&plot=short"
response = r.get(url)
movie_data = response.json()

release_year = ''

if y == '':
    release_year = movie_data['Year']
    print("Release Of Year", release_year)
else:
    release_year = y

director = movie_data['Director']
# content_type = movie_data['Type']

#  Fetch List of all actors
cast_list = findCast(movie_name, release_year)
if cast_list == 0:
    print("Program Stopped!")
else:
    # if cast List not empty
    print('Cast : ', cast_list)
    for actor in cast_list:
        main_code(actor)

    actor_avg_score = {}  # To save actor name along with its avg imdb rating of past 5 movies

    for i, j in actor_hist.items():
        score = []
        # i -> actor name
        # j -> movie name along with year in a dictionary

        if len(j) > 1:  # if the actor (i) has more than 1 movie under his belt
            for p, q in j.items():
                # Calling OMDB API to fetch imdb ratings
                # of last 5 movies of each actor
                url = "http://www.omdbapi.com/?apikey=" + omdb_api_key + "&t=" + str(p) + "&y=" + str(q) + "&plot=full"
                response = r.get(url)
                movie_data = response.json()

                if movie_data['Response'] == 'True':
                    if 'N' not in movie_data["imdbRating"]:
                        # Write a function to send json data as a parameter and returns Total Nominations

                        #  storing imdb score in a list
                        score.append(float(movie_data["imdbRating"]))
        # Find the average of best 3 movies
        score.sort()
        # Last 3 elements will be highest of all
        print(score)

        # score_sum = sum(score[2:])
        # avg = score_sum / 3

        # a function to extract the best movies out of total movies based on imdb
        actor_avg = extract_best_movies(score)

        print(f'Average rating of {i} : {actor_avg}')
        actor_avg_score.setdefault(i, actor_avg)
        print()

    best_actor_scores = []
    all_actor_scores = []
    for i, j in actor_avg_score.items():
        # cast avg score out of 5
        best_actor_scores.append(j / 2)
        print(f'{i} : %.2f' % j)
        all_actor_scores.append(j)

    print(f'All actor scores : {all_actor_scores}')

    best_actor_scores.sort()
    # best 3 cast out of 5
    # with avg scores in last 5 or less movies
    best_actor_scores = [best_actor_scores[-1], best_actor_scores[-2], best_actor_scores[-3]]
    print('\n')
    print(f'Best scores : {best_actor_scores}')
    # A function to extract a list of scores
    # of last 5 movies of a director by passing director name
    scoreOfMovies = director_main_code(director)

    # scoreOfMovies is score of movies of a director
    # director_avg -> stores the avg of best movies out of 5 or less
    director_avg = extract_best_movies(scoreOfMovies)
    director_avg = director_avg / 2

    p = ok = flop = 0
    for i in best_actor_scores:
        if 3.5 <= i <= 5:
            p = p + 1
        elif 3 <= i <= 3.5:
            ok = ok + 1
        else:
            flop = flop + 1

    dp = dok = dflop = 0
    i = director_avg
    if 3.5 <= i <= 5:
        dp = dp + 1
    elif 3 <= i <= 3.5:
        dok = dok + 1
    else:
        dflop = dflop + 1

    print('Based on cast popularity and past movies success')
    print('This movie will be ', end=" ")
    if p >= 2 and dp == 1:
        print("Hit")
    elif p >= 1 and dp == 1 and ok >= 1:
        print('Good')
    elif p >= 1 and ok >= 1 and dok == 1:
        print('Good or Average')
    else:
        print('Flop')
