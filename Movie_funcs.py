import requests as r
from datetime import date

"""
    This file is a list of all methods/functions used 
    to extract mainly information, using OMDB and TMDB websites,
    about actors and his/her movies, director's movies, along with scores - {IMDB Ratings}
"""

"""
    Function - 1

    To fetch actors list from a specific movie
    Using TMDB API

"""


def findCast(movie, year):
    url = "https://api.themoviedb.org/3/search/movie?api_key=001a39241eb26389e5bcf5f8f4bfa764&page=1&query=" + movie + "&include_adult=false&year=" + str(
        year)
    response = r.get(url)
    data = response.json()
    movie_data = data['results']
    # Grabbing the dictionary where movie id is present
    z = 0
    #  i is element of movie_data representing a dict
    for i in movie_data:
        if 'original_title' in i and i['original_title'] == movie:
            z = i
            break

    if z != 0:
        movie_id = z['id']
        # Calling same API again to fetch the cast list using movie_id
        url = "https://api.themoviedb.org/3/movie/" + str(
            movie_id) + "/credits?api_key=001a39241eb26389e5bcf5f8f4bfa764"
        response = r.get(url)
        data = response.json()
        c = 0
        cast = data['cast']
        actors = []

        """     Listing 5 top actors of this movie      """

        for actor in cast:
            if actor['known_for_department'] == 'Acting':
                actors.append(actor['name'])
                c = c + 1
            if c == 5:
                break
        return actors

    else:
        print("Movie Not found")
        return []


"""
    Function - 2

    Following Function to fetch Movie performance in terms of IMDB Ratings

    Step 1 -> Get actor name
    Step 2 -> Get last 5 movies name of release years less than rel year of searched movie
    Step 3 -> While listing 5 movies Get one movie, then check if it is a movie and person is the main cast,
                    -> if yes, then fetch imdb rating and store in a list

    Step 4 -> Sort score list and returns the score list

"""

"""
    movie_with_imdb ->  A dictionary that stores movie names along with imdb ratings 
    To avoid repeated api calls to fetch imdb rating for the same movie """

movie_with_imdb = {}


# Filtering one movie at a time by runtime and
# if the actor is the main cast in the movie
def filter_movies(movie, person):
    url = "http://www.omdbapi.com/?apikey=c4779b30&t=" + movie + "&plot=full"
    response = r.get(url)
    data = response.json()
    if data['Response'] == 'True':
        # print('Response : True')
        release_year = data['Year']
        # print(float(data['imdbRating']))
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

        for i in arranged_movies_list:
            # print(i['original_title'])
            if c == 5:
                break
            if 'release_date' in i:
                # print('Condition 1 -> checking release year...')
                yor = i['release_date'].split('-')
                rly = yor[0]
                # print(searched_movie_year, 'from movie_analysis.py')
                today = str(date.today()).split('-')
                # print(today, yor)
                # if searched_movie_year != '' and rly != '':
                if str(int(searched_movie_year) - 12) <= rly:
                    # print(searched_movie_year, rly, end=", ")
                    # print('Condition 2 -> checking lower limit of release year...')
                    # month no                # Day no.
                    """if rly <= today[0] and ((yor[1] <= today[1]) or (yor[2] <= today[2])):"""

                    """
                        cond3 satisfies that movies searched are movies release before user-entered movie   """
                    cond3 = False
                    # for release year less than current year
                    if yor[0] < today[0]:
                        cond3 = True
                    # for release year ==  current year
                    elif yor[0] == today[0] and ((yor[1] < today[1]) or (yor[2] <= today[2])):
                        cond3 = True

                    if cond3:
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
        # print()
        print('\n')
        return score

    else:
        print(f'{person} not found!')


def cast_score_main_code(person, searched_movie_year):
    actor = person
    cast_score = findmoviesByCast(actor, searched_movie_year)
    cast_score.sort()
    print(person)
    print(f'Last Movies Performance : {cast_score}')
    return cast_score


# main_code(input())


"""
    Function - 3

    Following Functions is to fetch last Movie Performances 
    of a Director in terms of {IMDB Ratings}
"""


def filter_director_movies(movie, director_name):
    """
        Following code check if movie is actually a movie performed by director
        By checking -> its runtime (must be at least 75 mins)
                    -> if the director_name is the director of movie
                    -> if IMDB rating present, stores it in a score list of past movies by Director
    """

    url2 = "http://www.omdbapi.com/?apikey=c4779b30&t=" + movie + "&plot=short"
    details = r.get(url2)
    movie_data = details.json()
    if movie_data['Response'] == 'True':
        # print('Response Accepted')
        if (director_name in movie_data['Director']) or (director_name in movie_data['Writer']):
            # print("Directed by", director_name)
            runtime = movie_data['Runtime']
            runtime = runtime[:runtime.find('m') - 1]
            if ('N' not in runtime) and int(runtime) >= 75:
                # print('Runtime Accepted')
                if 'N' not in movie_data['imdbRating']:
                    # print('IMDBRating achieved')
                    return float(movie_data['imdbRating'])

    return -1


def getDirectorPastMovie(direc_id, person):
    """
        Following Code fetch movie names
        where the director is involved
    """

    crew = r.get(
        "https://api.themoviedb.org/3/discover/movie?api_key=001a39241eb26389e5bcf5f8f4bfa764&language=en-US&sort_by=release_date.desc&include_adult=false&include_video=false&page=1&with_crew=" + direc_id + "&with_watch_monetization_types=flatrate")
    dataOfCrew = crew.json()
    n = 0
    score = []
    if len(dataOfCrew['results']) < 15:
        n = len(dataOfCrew['results'])
    else:
        n = 15

    for i in range(n):

        """
            filter_director_movies() shortlist the movies 
            By checking if director has directed this movie
        """
        # print(dataOfCrew['results'][i]['original_title'])
        z = filter_director_movies(dataOfCrew['results'][i]['original_title'], person)
        if z != -1:
            score.append(z)

        if len(score) == 5:
            break

    return score


def director_main_code(person):
    """      To fetch Director ID     """

    url = 'https://api.themoviedb.org/3/search/person?api_key=001a39241eb26389e5bcf5f8f4bfa764&query=' + person + '&language=en-US&page=1&include_adult=false'
    response = r.get(url)
    data = response.json()
    director_career = data['results']
    director_id = ''
    for i in director_career:
        director_id = i['id']
        break
    print('\n')

    if director_id != '':
        print(f'Director : {person}')

        """
         Following function returns a list of score of past movies of director    """

        scoreOfMovies = getDirectorPastMovie(str(director_id), person)

        scoreOfMovies.sort()
        print(scoreOfMovies)
        return scoreOfMovies

    else:
        print('Director Not found!')
        return []
