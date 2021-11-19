# this code returns a list of movies for each actor
# along with release year
# in dictionary -> actor_hist


import imdb
import requests as r

actor_hist = {}
director_hist = {}


def findMovies(person):
    print()
    print("file-2")
    print(person)
    print()
    movies = {}
    director_movies = {}
    # creating instance of IMDb
    ia = imdb.IMDb()

    name = person
    # movies = {}
    # director_movies = {}
    # searching the name
    search = ia.search_person(name)

    # to extract actor detail list
    def extract_person_info(actor_results):
        for x, y in actor_results.items():
            # print(actor_results['data']['name'])
            return actor_results['data']
        return {}

    info = {}
    for i in range(len(search)):
        # extracting person ID
        person_id = search[i].personID

        #  fetching actor details using person_ID
        actor_results = ia.get_person_filmography(person_id)

        # calling a function to fetch all movie list, name, birthplace
        info = extract_person_info(actor_results)
        if info != {}:
            break

    # if info not empty
    # if info != {} and 'actor' in info['filmography']:
    if info != {}:
        if 'actor' in info['filmography']:
            role = 'actor'
        elif 'actress' in info['filmography']:
            role = 'actress'
        elif 'director' in info['filmography']:
            role = 'director'
        elif 'writer' in info['filmography']:
            role = 'writer'
        # else:

        movie_count = 0
        #  list of movies (j) performed by the actor/director/writer
        for j in info['filmography'][role]:
            if movie_count == 5:
                if role == 'director':
                    director_hist[person] = director_movies
                # saving actor name along with movies list
                else:
                    actor_hist[person] = movies
                return

            #  To fetch year of release from omdb api

            url = "http://www.omdbapi.com/?apikey=c4779b30&t=" + str(j) + "&plot=full"
            response = r.get(url)
            data = response.json()

            def filter_movies(j, data, role):
                # Filtering movie list with runtime
                runtime = data['Runtime']
                runtime = runtime[:runtime.find('m') - 1]
                if 'Year' in data and ('N' not in runtime) and int(runtime) >= 75:
                    year = data['Year']
                    if len(year) == 4 and int(year) < 2021:
                        # saving movie name along with year in movies dictionary
                        if role == 'director':
                            director_movies[j] = year
                        else:
                            print(j, year)
                            movies.setdefault(j, year)
                        return 1
                return 0

            if 'Runtime' in data and person in data['Actors']:
                movie_count = movie_count + filter_movies(j, data, role)
                print('Movie Count : ', movie_count)

            elif 'Runtime' in data and person in data['Director']:
                movie_count = movie_count + filter_movies(j, data, role)

        if len(info['filmography'][role]) <= 5:
            if role == 'director':
                director_hist[person] = director_movies
            else:
                actor_hist[person] = movies
            return

    else:
        print(f'{person} Not found!')
