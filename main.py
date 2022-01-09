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
from Movie_funcs import *
from datetime import date
from window import *


# def display_message(msg, x, y):
#     canvas.create_text(x, y, text=msg, font=("Poppins", 20), fill="white")


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
    print()
    # Fetching api keys from different websites

    # omdb_api_key = os.environ.get('OMDB_API')
    # tmdb_api_key = os.environ.get('MOVIE_API')

    # movie_name, y = input_from_user()

    """
        From OMDB website to fetch release year,
        all kinds of ratings,
        awards,
        cast and director and type
    """

    # display_message('Fetching Data...', 630, 250)

    url = "http://www.omdbapi.com/?apikey=c4779b30&t=" + movie_name + "&y=" + str(y) + "&plot=short"
    response = r.get(url)
    movie_data = response.json()
    if movie_data['Response'] == 'False':
        return movie_data['Error']

    release_year = ''

    if y == '':
        release_year = movie_data['Year']
        print("Release Of Year", release_year)

    elif y != '' and not y.isnumeric():
        return 'Invalid Release Year'

    else:
        release_year = y

    director = movie_data['Director']
    # print(director)

    movie_name = movie_data['Title']
    print(movie_name, y)

    #  Fetch List of all actors
    cast_list = findCast(movie_name, release_year)

    # if cast List couldn't be found from TMDB website
    if not cast_list:
        if 'N/A' not in movie_data['imdbID']:
            print('From IMDB Website')
            cast_list = find_Cast_From_Imdb(movie_data['imdbID'])
            if not cast_list:
                print("Program Stopped!")
                return 'Movie Not Found!'
        else:
            print("Program Stopped!")
            return 'Movie Not Found!'

    # if cast List not empty
    actor_performance = {}
    print('Cast : ', cast_list)
    for actor in cast_list:
        # returns score list of past movies
        score = cast_score_main_code(actor, release_year)
        actor_avg = extract_best_movies(score)
        # storing actor's average score along with no. of movies (MAX : 5)
        actor_performance.setdefault(actor_avg, len(score))

    # Score preference based on no. of movies and score
    count_newbies = 0
    best_actor_scores = []
    # avg_score_list = []

    # For loop to accept experienced actors first
    for i, j in actor_performance.items():
        # i -> avg score of an actor
        # j -> no. of movies (MAX 5)
        if j >= 4:
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
    director_avg = 0
    scoreOfMovies = []
    if ',' in director:
        director = director.split(', ')
        sum_of_more_directors = 0
        for direc_person in director:
            scoreOfMovies = director_main_code(direc_person)
            sum_of_more_directors += extract_best_movies(scoreOfMovies)

        director_avg = sum_of_more_directors / len(director)
    else:
        scoreOfMovies = director_main_code(director)
        # scoreOfMovies is score of movies of a director
        # stores the avg of best movies out of 5 or less
        director_avg = extract_best_movies(scoreOfMovies)

    """ Upto above code"""

    """
        The Following Code -> Grading System
    """

    # best 3 actor chosen out of 5
    p = gd = ok = flop = 0
    for i in best_actor_scores:
        print('%.2f' % i)
        if 7.8 <= i:
            # p counts no. of good actors
            p = p + 1
        elif 7 < i < 7.8:
            gd = gd + 1
        elif 6 <= i <= 7:
            # ok counts no. of average actors
            ok = ok + 1
        elif i < 6:
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

    print('Popular Actors : ', p)
    print('Good Actors : ', gd)
    print('Average Actors : ', ok)
    print('Flop actors : ', flop)
    print('Based on cast and director popularity and past movies success')
    print('This movie will be', end=" ")
    if dp == 1:
        # more than 8
        if p >= 2 and flop == 0 and ok == 0:
            return 'Super-Hit'

        # less than 8 and more than 7
        elif gd >= 2 and flop == 0:
            return 'Hit'

        elif gd >= 1 and ok >= 1 and flop == 0:
            return 'Hit'

    elif dok == 1:
        # less than 7 but more than 6
        if gd == 3 or (p + gd == 3):
            return 'Above Average'

        if (ok + gd) == 3:
            return 'Average'

        if ok >= 1 and (p + gd + ok) == 3:
            return 'Average'

        if ok == 3:
            return 'Below Average'

    elif dflop == 1:
        if p >= 1 or ok > 1:
            return 'Below Average'

    # less than 6 but more than 5
    elif (p >= 1 and dflop == 1) or (ok > 1 and dflop == 1):
        return 'Below Average'

    # less than 5
    else:
        return 'Flop'


print(main_file_run(input("Enter Movie Name: "), input("Enter release year : ")))
