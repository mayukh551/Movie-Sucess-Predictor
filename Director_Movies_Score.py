import time

import requests as r

# scoreOfMovies = []


def get_imdb_rating(movies, director):
    score = []
    for movie in movies.keys():
        url2 = "http://www.omdbapi.com/?apikey=c4779b30&t=" + movie + "&plot=short"
        details = r.get(url2)
        movie_data = details.json()
        if movie_data["Response"] == 'True':
            score.append(float(movie_data["imdbRating"]))

    score.sort()
    return score


def filter_director_movies(movies, director_name):
    final_movies_list = {}
    c = 0
    for_start_time = time.time()
    for movie in movies:
        if c == 5:
            break
        url2 = "http://www.omdbapi.com/?apikey=c4779b30&t=" + movie + "&plot=short"
        details = r.get(url2)
        movie_data = details.json()
        if movie_data['Response'] == 'True':
            if movie_data['Director'] == director_name:
                runtime = movie_data['Runtime']
                runtime = runtime[:runtime.find('m') - 1]
                if ('N' not in runtime) and int(runtime) >= 75:
                    final_movies_list.setdefault(movie, movie_data['Year'])
                    c = c + 1
    for_end_time = time.time()
    print(f'Time Taken by for loop in filter movies() : {for_end_time - for_start_time}')
    return final_movies_list


def getDirectorPastMovie(direc_id):
    crew = r.get(
        "https://api.themoviedb.org/3/discover/movie?api_key=001a39241eb26389e5bcf5f8f4bfa764&language=en-US&sort_by=release_date.desc&include_adult=false&include_video=false&page=1&with_crew=" + direc_id + "&with_watch_monetization_types=flatrate")
    dataOfCrew = crew.json()
    direc_movie_list = []
    n = 0
    if len(dataOfCrew['results']) < 15:
        n = 10
    elif len(dataOfCrew['results']) < 10:
        n = 5
    else:
        n = 15
    for i in range(n):
        direc_movie_list.insert(i, dataOfCrew['results'][i]['original_title'])
        # direc_movie_list.append(dataOfCrew['results'][i]['original_title'])
    return direc_movie_list


# print(getDirectorPastMovie('525'))
# print(getDirectorPastMovie('7467'))

def director_main_code(person):
    # person = input("Enter director's name : ")
    url = 'https://api.themoviedb.org/3/search/person?api_key=001a39241eb26389e5bcf5f8f4bfa764&query=' + person + '&language=en-US&page=1&include_adult=false'
    response = r.get(url)
    data = response.json()
    director_career = data['results']
    director_id = ''
    for i in director_career:
        director_id = i['id']
        break
    print(f'Director ID : {director_id}')
    print('\n')
    if director_id != '':
        director_movies_list = getDirectorPastMovie(str(director_id))
        for i in director_movies_list:
            print(i)
        movies_by_director = filter_director_movies(director_movies_list, person)
        print()
        for i, j in movies_by_director.items():
            print(i, j)
        scoreOfMovies = get_imdb_rating(movies_by_director, person)
        print(scoreOfMovies)
        return scoreOfMovies

    else:
        print('Director Not found!')
