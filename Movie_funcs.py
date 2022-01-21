from bs4 import BeautifulSoup
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


# 609af948


def find_Cast_From_Imdb(imdb_id):
    imdb_url = 'https://www.imdb.com/title/' + str(imdb_id) + '/'
    source = r.get(imdb_url)
    cast_list = []
    # print(source.text)
    # print('\n\n')
    if source.status_code == 200:
        # print('working\n')
        soup = BeautifulSoup(source.text, 'html.parser')
        cast_data = soup.find('div', class_="title-cast__grid").find_all('div',
                                                                         class_="StyledComponents__CastItemWrapper-sc-y9ygcu-7")
        for actor in cast_data:
            cast_list.append(
                actor.find('div', class_="StyledComponents__CastItemSummary-sc-y9ygcu-9 hLoKtW").find('a').text)
            if len(cast_list) == 5:
                return cast_list

        return cast_list

    else:
        return None


def findCast(movie, year):
    # Kitchen
    url = "https://api.themoviedb.org/3/search/movie?api_key=001a39241eb26389e5bcf5f8f4bfa764&page=1&query=" + movie + "&include_adult=false&year=" + str(
        year)
    # Food served on plate
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

imdb_rating_cache = {}


def cast_score_main_code(person, searched_movie_year):
    # to fetch the person id
    print('*******************************\n')
    print('Actor/Actress : ', person)
    print()
    print('Movie performed by', person, ':')
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
        # imdb_id
        # print(person_id)
        url = 'https://api.themoviedb.org/3/person/' + str(
            person_id) + '?api_key=001a39241eb26389e5bcf5f8f4bfa764&language=en-US'

        imdb_id = r.get(url).json()['imdb_id']
        url = 'https://www.imdb.com/name/' + imdb_id
        source = r.get(url)
        if source.status_code == 200:
            soup = BeautifulSoup(source.text, 'html.parser')
            movies = soup.find('div', id="filmography").find('div', class_="filmo-category-section").find_all('div',
                                                                                                              class_="filmo-row")
            c = 0
            score = []

            for movie in movies:
                if c == 5:
                    break

                if "(" not in movie.text and ")" not in movie.text:
                    movie_name = movie.find('a').text
                    y = movie.find('span', class_="year_column").text[2:-1]
                    if movie_name in imdb_rating_cache:
                        print('Same movie performed by another actor')
                        score.append(imdb_rating_cache[movie_name])
                        c = c + 1
                    # print(y)
                    elif y[:4].isnumeric():
                        url = "http://www.omdbapi.com/?apikey=609af948&t=" + movie_name + "&y=" + str(
                            y) + "&plot=short"
                        data = r.get(url).json()
                        if data['Response'] == 'True' and 'N' not in data['imdbRating']:
                            imdbRating = float(data['imdbRating'])
                            print(movie_name, y[:4], imdbRating)
                            imdb_rating_cache.setdefault(movie_name, imdbRating)
                            score.append(imdbRating)
                            c = c + 1

            score.sort()
            print(f'Last Movies Performance of {person} : {score}')
            print('\n')
            return score


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

    url2 = "http://www.omdbapi.com/?apikey=609af948&t=" + movie + "&plot=short"
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
    """   To fetch Director ID     """

    print('*******************************')
    print()

    url = 'https://api.themoviedb.org/3/search/person?api_key=001a39241eb26389e5bcf5f8f4bfa764&query=' + person + '&language=en-US&page=1&include_adult=false'
    response = r.get(url)
    data = response.json()
    director_career = data['results']
    director_id = ''
    for i in director_career:
        director_id = i['id']
        break
    # print('\n')

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
