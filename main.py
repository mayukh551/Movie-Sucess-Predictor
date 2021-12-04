"""
    This is the main python file...

    ->  It gets the historical data of actors and directors
        of the movie searched by the user

    ->  And then based on their average score and best performances,
        It is checked how famous, good, or flop these actors or directors are...

    ->  Based on these factors, a movie is rated as hit/good/average/flop

"""

import requests as r
import os
from Get_Actor_List import *
from Director_Movies_Score import *
from Get_Cast_Score import *


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

'''
From OMDB website to fetch release year,
all kinds of ratings,
awards,
cast and director and type'''

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

#  Fetch List of all actors
cast_list = findCast(movie_name, release_year)
if len(cast_list) == 0:
    print("Program Stopped!")
    cast_list = movie_data['Actors']
else:
    score = []
    actor_score = {}
    # if cast List not empty
    score_pref = {}
    actor_performance = {}
    print('Cast : ', cast_list)
    for actor in cast_list:
        # returns score list of past movies
        score = main_code(actor)
        actor_avg = extract_best_movies(score)
        # storing actor's average score along with no. of movies (MAX : 5)
        actor_performance.setdefault(actor_avg, len(score))

    # Score preference based on no. of movies and score
    count_newbies = 0
    best_actor_scores = []

    # For loop to accept experienced actors first
    for i, j in actor_performance.items():
        # i -> avg score of an actor
        # j -> no. of movies (MAX 5)
        if j > 4:
            best_actor_scores.append(i / 2)

    # Checking if cast list have experienced actors
    if len(best_actor_scores) > 1:
        # Scores arranged in descending order
        best_actor_scores.sort(reverse=True)

        if len(best_actor_scores) >= 3:
            best_actor_scores = best_actor_scores[:3]

    # if there is lack of experienced actors
    # newbies are considered
    if len(best_actor_scores) < 3:
        for i, j in actor_performance.items():
            # actors with less experience
            if j < 4:
                best_actor_scores.append(i / 2)
            if len(best_actor_scores) == 3:
                break

    # A function to extract a list of scores
    # of last 5 movies of a director by passing director name
    scoreOfMovies = director_main_code(director)

    # scoreOfMovies is score of movies of a director
    # stores the avg of best movies out of 5 or less
    director_avg = extract_best_movies(scoreOfMovies)
    director_avg = director_avg / 2

    # best 3 actor chosen out of 5
    p = ok = flop = 0
    for i in best_actor_scores:
        if 3.5 <= i <= 5:
            # p counts no. of good actors
            p = p + 1
        elif 3 <= i <= 3.5:
            # ok counts no. of average actors
            ok = ok + 1
        else:
            # flop counts no. of flop actors
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
        print('Above Average')
    elif p >= 1 or dp == 1:
        print('Average')
    elif p >= 1 and dok == 1:
        print('Below Average')
    else:
        print('Flop')

    # # a function to extract the best movies out of total movies based on imdb
    # actor_avg = extract_best_movies(score)
    #
    # print(f'Average rating of {i} : {actor_avg}')
    # actor_avg_score.setdefault(i, actor_avg)
    # print()
    #
    # best_actor_scores = []
    # all_actor_scores = []
    # for i, j in actor_avg_score.items():
    #     # cast avg score out of 5
    #     best_actor_scores.append(j / 2)
    #     print(f'{i} : %.2f' % j)
    #     all_actor_scores.append(j)
    #
    # print(f'All actor scores : {all_actor_scores}')
    #
    # best_actor_scores.sort()
    # # best 3 cast out of 5
    # # with avg scores in last 5 or less movies
    # best_actor_scores = [best_actor_scores[-1], best_actor_scores[-2], best_actor_scores[-3]]
    # print('\n')
    # print(f'Best scores : {best_actor_scores}')
    # # A function to extract a list of scores
    # # of last 5 movies of a director by passing director name
    # scoreOfMovies = director_main_code(director)
    #
    # # scoreOfMovies is score of movies of a director
    # # director_avg -> stores the avg of best movies out of 5 or less
    # director_avg = extract_best_movies(scoreOfMovies)
    # director_avg = director_avg / 2
    #
    # p = ok = flop = 0
    # for i in best_actor_scores:
    #     if 3.5 <= i <= 5:
    #         p = p + 1
    #     elif 3 <= i <= 3.5:
    #         ok = ok + 1
    #     else:
    #         flop = flop + 1
    #
    # dp = dok = dflop = 0
    # i = director_avg
    # if 3.5 <= i <= 5:
    #     dp = dp + 1
    # elif 3 <= i <= 3.5:
    #     dok = dok + 1
    # else:
    #     dflop = dflop + 1
    #
    # print('Based on cast popularity and past movies success')
    # print('This movie will be ', end=" ")
    # if p >= 2 and dp == 1:
    #     print("Hit")
    # elif p >= 1 and dp == 1 and ok >= 1:
    #     print('Good')
    # elif p >= 1 and ok >= 1 and dok == 1:
    #     print('Good or Average')
    # else:
    #     print('Flop')
