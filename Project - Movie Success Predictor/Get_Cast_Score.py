"""
Step 1 -> Get actor name
Step 2 -> Get last 5 movies name of release years less than rel year of searched movie
Step 3 -> While listing 5 movies Get one movie, then check if it is a movie and person is the main cast,
                -> if yes, then fetch imdb rating and store in a list

Step 4 -> Sort score list and returns the score list

"""

import requests as r
from Get_Actor_List import *
from datetime import date

'''
    A dictionary that stores movie names along with imdb ratings 
    To avoid repeated api calls to fetch imdb rating for the same movie
'''
movie_with_imdb = {}


# Filtering one movie at a time by runtime and
# if the actor is the main cast in the movie
def filter_movies(movie, person):
    url = "http://www.omdbapi.com/?apikey=c4779b30&t=" + movie + "&plot=full"
    response = r.get(url)
    data = response.json()
    if data['Response'] == 'True':
        release_year = data['Year']
        # find the main cast of the movies
        # findCast is a function from Get_Actor_List.py file
        main_cast = findCast(movie, release_year)
        if person in main_cast:
            runtime = data['Runtime']
            runtime = runtime[:runtime.find('m') - 1]
            if ('N' not in runtime) and int(runtime) >= 75:
                # It is a movie where person is a main cast
                if 'N' not in data['imdbRating']:
                    return float(data['imdbRating'])

    return -1


#  Fetching a list of movies the actor has ever appeared
# then it will be sent to filter_movies() to for shortlisting the list

def findmoviesByCast(person, searched_movie_year):
    # To store list of imdb ratings from past movies for this actor
    score = []
    # to fetch the person id
    url = 'https://api.themoviedb.org/3/search/person?api_key=001a39241eb26389e5bcf5f8f4bfa764&query=' + person + '&language=en-US&page=1&include_adult=false'
    response = r.get(url)
    data = response.json()
    cast_data = data['results']
    person_id = ''
    for i in cast_data:
        person_id = i['id']
        break

    # if person_id not empty
    if person_id != '':
        # print(person, ':', person_id)
        # to fetch the list of movies performed by the user
        url = 'https://api.themoviedb.org/3/discover/movie?api_key=001a39241eb26389e5bcf5f8f4bfa764&language=en-US&with_cast=' + str(
            person_id) + '&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate'
        response = r.get(url)
        data = response.json()
        # creating the movie list of this actor
        c = 0
        lis = data['results']
        arranged_movies_list = []
        try:
            arranged_movies_list = sorted(lis, key=lambda x: x['release_date'], reverse=True)
        except KeyError:
            arranged_movies_list = lis
        # for i in data['results']:
        for i in arranged_movies_list:
            # print(i['original_title'])
            if c == 5:
                break
            if 'release_date' in i:
                # print('Condition 1 -> checking release year...')
                yor = i['release_date']
                rly = yor[:4]
                today = str(date.today())
                # print(searched_movie_year, 'from movie_analysis.py')
                # if searched_movie_year != '' and rly != '':
                # <= (int(searched_movie_year) + 1)
                if str(int(searched_movie_year) - 12) <= rly:
                    # print(searched_movie_year, rly, end=", ")
                    # print('Condition 2 -> checking lower limit of release year...')
                    # month no                # Day no.
                    if rly <= today[:4] and ((yor[5:7] <= today[5:7]) or (yor[8:] <= today[8:])):
                        # Fetch imdb rating
                        # print('Condition 3 -> checking upper limit of release year')
                        if i['original_title'] in movie_with_imdb:
                            print('Same movie performed by another actor')
                            score.append(movie_with_imdb[i['original_title']])
                            c = c + 1
                        else:
                            z = filter_movies(i['original_title'], person)
                            if z != -1:
                                print(i['original_title'], end=", ")
                                movie_with_imdb.setdefault(i['original_title'], z)
                                c = c + 1
                                # print(f'Final condition -> if it is a movie_#{c}')
                                score.append(z)
        print()
        print('\n')
        return score

    else:
        print(f'{person} not found!')


def main_code(person, searched_movie_year):
    actor = person
    cast_score = findmoviesByCast(actor, searched_movie_year)
    cast_score.sort()
    print(person)
    print(f'Last Movies Performance : {cast_score}')
    return cast_score

# main_code(input())
