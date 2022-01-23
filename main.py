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


# 609af948
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
        From OMDB website to fetch release year(if required),
        movie title
        imdb ratings,
        cast and director and type
    """

    # If user does not give the name of movie or any input
    if movie_name == "":
        return 'Invalid Input!'

    # if user has entered released year
    if y != '' and not y.isnumeric():
        return 'Invalid Release Year'

    url = "http://www.omdbapi.com/?apikey=609af948&t=" + movie_name + "&y=" + str(y) + "&plot=short"
    response = r.get(url)
    # print(type(response))
    # print(response.text)
    movie_data = response.json()
    if movie_data['Response'] == 'False':
        return movie_data['Error']

    # The movie has already been released with imdb rating available
    if 'N/A' not in movie_data['imdbRating']:
        if len(movie_data['Year']) > 4:
            return 'Not a Movie!'
        else:
            return movie_data['imdbRating']

    release_year = ''

    # if user has not entered the release year
    # release year of the movie is fetched from OMDB website
    if y == '':
        release_year = movie_data['Year']
        print(release_year)
        if len(release_year) > 4:
            return 'Not a Movie!'
        print("Release Of Year", release_year)

    else:
        release_year = y

    """ After all test cases validation,
        Further data extraction begins 
    """

    director = movie_data['Director']

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
                return 'Movie Not Found!'
        else:
            return 'Movie Not Found!'

    # if cast List not empty
    actor_performance = {}
    print('Cast : ', cast_list)
    print()
    best_actor_scores = []
    for actor in cast_list:
        score = cast_score_main_code(actor, release_year)
        actor_avg = extract_best_movies(score)
        best_actor_scores.append(float(actor_avg))

    best_actor_scores.sort(reverse=True)
    best_actor_scores = best_actor_scores[:3]

    # A function to extract a list of scores
    # of last 5 movies of a director by passing director name
    director_avg = 0
    scoreOfMovies = []

    # if more than 1 director present
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
    print()
    print('Average imdb score of best 3 chosen out of 5 actors : ')
    for i in best_actor_scores:
        print('%.2f' % i, end=" ")
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

    print()

    dp = dok = dflop = 0
    print('Director Average Imdb Score : %.2f' % director_avg)
    i = director_avg
    if 7 < i:
        dp = 1
    elif 6 <= i < 7:
        dok = 1
    else:
        dflop = 1

    print('Popular Actors : ', p)
    print('Good Actors : ', gd)
    print('Average Actors : ', ok)
    print('Flop actors : ', flop)
    print('Based on cast and director popularity and past movies success')
    print('This movie will be', end=" ")

    """
        ****************************************************
        
    For good directors, possible conditions      """

    if dp == 1:
        if p == 3:
            return 'Super-Hit'

        elif (p + gd) == 3:
            """ popular and good -> 
                2 cases ->  1. p > gd 
                            2. gd > p       """
            return 'Hit'

        elif (p + gd) == 3:
            """ popular and ok -> 
                2 cases ->   1. p > ok
                             2. ok > p   """
            if p > ok:
                return 'Hit'

            elif ok > p:
                return 'Above Average'

        elif (p + flop) == 3:
            """ popular and flop ->
                1 case ->   p > flop       """

            if p > flop:
                return 'Hit'

            elif flop > p:
                return 'Above Average'

        elif gd == 3:
            return 'Hit'

        elif (gd + ok) == 3:
            """ Possible combinations with Good   """
            if gd > ok:
                return 'Hit'

            elif ok > gd:
                return 'Above Average'

        elif (gd + flop) == 3:
            if gd > flop:
                return 'Above Average'

            elif flop > gd:
                return 'Average'

        elif ok == 3:
            return 'Average'

        elif (ok + flop) == 3:
            if ok > flop:
                return 'Average'

            elif flop > ok:
                return 'Below Average'

        elif flop == 3:
            return 'Below Average'

        # popular, good, ok combination

        elif (p + gd + ok) == 3:
            return 'Hit'

        elif (p + gd + flop) == 3:
            return 'Hit'

        elif (flop + gd + ok) == 3:
            return 'Above Average'

    """
           ****************************************************

       For average directors, possible conditions      """

    if dok == 1:

        # Popular Actors under Average Actors

        if p == 3:
            return 'Hit'

        if (p + gd) == 3:
            """ popular and good -> 
                2 cases ->  1. p > gd 
                            2. gd > p       """
            if p > gd:
                return 'Hit'

            elif gd > p:
                return 'Above Average'

        elif (p + ok) == 3:
            """ popular and ok -> 
                2 cases ->   1. p > ok
                            2. ok > p   """
            if p > ok:
                return 'Above Average'

            elif ok > p:
                return 'Average'

        elif (p + flop) == 3:
            """ popular and flop ->
                1 case ->   p > flop       """

            if p > flop:
                return 'Average'

            elif flop > p:
                return 'Below Average'

        # Good actors under average Director

        elif gd == 3:
            return 'Above Average'

        if (gd + ok) == 3:
            """ Possible combinations with Good   """
            if gd > ok:
                return 'Above Average'

            elif ok > gd:
                return 'Average'

        elif (gd + flop) == 3:
            if gd > flop:
                return 'Below Average'

            elif flop > gd:
                return 'Flop'

        # Average actors under average Director

        elif ok == 3:
            return 'Below Average'

        elif (ok + flop) == 3:

            if ok > flop:
                return 'Below Average'

            elif flop > ok:
                return 'Flop'

        # Flop actors under average Director
        elif flop == 3:
            return 'Flop'

        # popular, good, ok, flop combination

        elif (p + gd + ok) == 3:
            return 'Above Average'

        elif (p + gd + flop) == 3:
            return 'Average'

        elif (flop + gd + ok) == 3:
            return 'Below Average'

    """*************************************************************
    
    For Flop directors, all possible combinations
    """

    if dflop == 1:

        # Popular actors combinations under flop directors

        if p == 3:
            return 'Above Average'

        if (p + gd) == 3:
            """ popular and good -> 
                2 cases ->  1. p > gd 
                            2. gd > p       """
            return 'Average'

        elif (p + ok) == 3:
            """ popular and ok -> 
                2 cases ->   1. p > ok
                            2. ok > p   """
            if p > ok:
                return 'Average'

            elif ok > p:
                return 'Below Average'

        elif (p + flop) == 3 and flop != 0 and p != 0:
            """ popular and flop ->
                1 case ->   p > flop       """

            if p > flop:
                return 'Average'

            else:
                return 'Below Average'

        # Good actors combinations under flop directors

        elif gd == 3:
            return 'Average'

        if (gd + ok) == 3:
            """ Possible combinations with Good   """
            if gd > ok:
                return 'Average'

            elif ok > gd:
                return 'Average'

        elif (gd + flop) == 3:
            if gd > flop:
                return 'Average'

            elif flop > gd:
                return 'Below Average'

        # Average actors combinations under flop director
        elif ok == 3 or (ok + flop) == 3 or flop == 3:
            return 'Flop'

        # popular, good, ok, flop combination

        elif (p + gd + ok) == 3:
            return 'Average'

        elif (p + gd + flop) == 3:
            return 'Below Average'

        elif (flop + gd + ok) == 3:
            return 'Flop'


# print(main_file_run(input("Enter Movie Name: "), input("Enter release year : ")))
