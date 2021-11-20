#  This code is to extract a list
#  of last 5 movies performed by an actor


import requests as r
from Get_Actor_List import *
import time

actor_hist = {}


# Filtering movies by runtime and
# if the actor is the main cast in the movie
def filter_movies(movies, person):
    filtered_movie_list = {}
    print('in function 2')
    t1 = t2 = 0
    for movie in movies:
        # part 1
        start = time.time()
        url = "http://www.omdbapi.com/?apikey=c4779b30&t=" + movie + "&plot=full"
        response = r.get(url)
        data = response.json()
        end = time.time()
        t1 = t1 + (end - start)
        if 'Year' in data:
            # part 2
            start = time.time()
            release_year = data['Year']
            main_cast = findCast(movie, release_year)
            # print(f'Main cast for {movie}')
            # print(*main_cast)
            if len(release_year) == 4:
                # print(release_year)
                if int(release_year) < 2021 and person in main_cast:
                    runtime = data['Runtime']
                    runtime = runtime[:runtime.find('m') - 1]
                    if ('N' not in runtime) and int(runtime) >= 75:
                        filtered_movie_list.setdefault(movie, release_year)
            end = time.time()
            t2 = t2 + (end - start)
            # print(f'Time taken by Part 2 = {end - start}')
    print(f'Time taken by part 1 = {t1}')
    print(f'Time taken by part 2 = {t2}')
    return filtered_movie_list


#  Fetching a list of movies the actor has ever appeared
# then it will be sent to filter_movies() to for shortlisting the list
def findmoviesByCast(person):
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
        movie_list = []
        # to fetch the list of movies performed by the user
        url = 'https://api.themoviedb.org/3/discover/movie?api_key=001a39241eb26389e5bcf5f8f4bfa764&language=en-US&with_cast=' + str(
            person_id) + '&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate'
        response = r.get(url)
        data = response.json()
        # creating the movie list of this actor
        for i in data['results']:
            movie_list.append(i['original_title'])
        return movie_list
    else:
        print('Actor not found!')


def main_code(person):
    actor = person
    start = time.time()

    movies_by_person = findmoviesByCast(actor)
    end = time.time()
    print(f'Time taken by function 1 = {end - start}')

    start = time.time()
    movies_list = filter_movies(movies_by_person, actor)
    end = time.time()
    print(f'Time taken by function 2 = {end - start}')

    main_start = time.time()

    # Following code arranges the movies w.r.t to release year
    # and chooses the last five movies
    # in which the actor has appeared as a main cast
    rel_year = movies_list.values()
    rel_year = sorted(rel_year, reverse=True)
    final_movie_list = []
    movie_count = 0
    z = 0
    years = []
    while movie_count < 5 and z < len(rel_year):
        for i, j in movies_list.items():
            if j == rel_year[z] and i not in final_movie_list:
                final_movie_list.append(i)
                years.append(j)
                movie_count += 1
        z = z + 1

    if len(final_movie_list) > 5:
        final_movie_list = final_movie_list[:5]
    if len(years) > 5:
        years = years[:5]
    final_movie_dict = {}
    print('Final list of movies : ')
    for i, j in zip(final_movie_list, years):
        final_movie_dict.setdefault(i, j)
        print(i, j)

    actor_hist.setdefault(person, final_movie_dict)

    main_end = time.time()
    print(f'Time taken by rest of main code = {main_end - main_start}')


main_code(input())
