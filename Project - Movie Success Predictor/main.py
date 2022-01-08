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



def main_file_run(movie_name, y):
    # Fetching api keys from different websites

    omdb_api_key = os.environ.get('OMDB_API')
    tmdb_api_key = os.environ.get('MOVIE_API')

    '''
    From OMDB website to fetch release year,
    all kinds of ratings,
    awards,
    cast and director and type'''

    # + omdb_api_key +

    # movie_name = input("Enter the movie name : ")
    # y = input("Enter the release year: ")
    print('file-1')
    print(movie_name, y)
    url = "http://www.omdbapi.com/?apikey=c4779b30&t=" + movie_name + "&y=" + str(y) + "&plot=short"
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
            score = main_code(actor, release_year)
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
                best_actor_scores.append(i)

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
                    best_actor_scores.append(i)
                if len(best_actor_scores) == 3:
                    break

        # A function to extract a list of scores
        # of last 5 movies of a director by passing director name
        scoreOfMovies = director_main_code(director)

        # scoreOfMovies is score of movies of a director
        # stores the avg of best movies out of 5 or less
        director_avg = extract_best_movies(scoreOfMovies)
        director_avg = director_avg

        # best 3 actor chosen out of 5
        p = gd = ok = flop = 0
        for i in best_actor_scores:
            if 8 <= i:
                # p counts no. of good actors
                p = p + 1
            elif 7 <= i < 8:
                gd = gd + 1
            elif 6 <= i < 7:
                # ok counts no. of average actors
                ok = ok + 1
            else:
                # flop counts no. of flop actors
                flop = flop + 1

        dp = dok = dflop = 0
        i = director_avg
        if 7 <= i:
            dp = dp + 1
        elif 6 <= i < 7:
            dok = dok + 1
        else:
            dflop = dflop + 1

        print('Based on cast and director popularity and past movies success')
        print('This movie will be', end=" ")
        if dp == 1:
            # more than 8
            if p >= 2 and flop == 0:
                print("Hit")
                return 'Hit'

            # less than 8 and more than 7
            elif p == 1 and gd == 2:
                print('Good')

            elif p >= 1 and ok >= 1 and flop == 0:
                print('Good')

            return 'Good'

        elif dok == 1:
            # less than 7 but more than 6
            if p >= 1 or ok >= 2 or gd >= 2:
                print('Average')
                return 'Average'

        elif dflop == 1:
            if p >= 1 or ok > 1:
                print('Below Average')
                return 'Below Average'

        # less than 6 but more than 5
        elif (p >= 1 and dflop == 1) or (ok > 1 and dflop == 1):
            print('Below Average')
            return 'Below Average'

        # less than 5
        else:
            print('Flop')
            return 'Flop'

# main_file_run(input("Enter the movie name : "),input("Enter the release year: "))

# if p >= 2 and dp == 1:
#     print("Hit")
#
# # less than 8 and more than 7
# elif p >= 1 and dp == 1 and ok >= 1:
#     print('Good')
#
# # less than 7 but more than 6
# elif (p >= 1 and dok == 1) or (ok >= 2 and dok == 1):
#     print('Average')
#
# # less than 6 but more than 5
# elif (p >= 1 and dflop == 1) or (ok > 1 and dflop == 1):
#     print('Below Average')
#
# # less than 5
# else:
#     print('Flop')
