import imdb
import requests as r


def findMovies(actor):
    # creating instance of IMDb
    ia = imdb.IMDb()

    name = actor

    # searching the name
    search = ia.search_person(name)
    country = 'India'

    # to extract actor detail list
    def extract_person_info(actor_results):
        for x, y in actor_results.items():
            if actor_results['data']['name'] == name:
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
    if info != {}:
        if 'actor' in info['filmography']:
            role = 'actor'
        elif 'writer' in info['filmography']:
            role = 'writer'
        elif 'director' in info['filmography']:
            role = 'director'

        movies = {}
        movie_count = 0
        #  list of movies performed by the actor/director/writer
        for j in info['filmography'][role]:

            if movie_count == 5:
                return

            #  To fetch year of release from omdb api

            url = "http://www.omdbapi.com/?apikey=c4779b30&t=" + str(j) + "&plot=full"
            response = r.get(url)
            data = response.json()
            if 'Runtime' in data and actor in data['Actors']:
                runtime = data['Runtime']
                runtime = runtime[:runtime.find('m') - 1]
                if 'Year' in data and ('N' not in runtime) and int(runtime) >= 75:
                    if len(data['Year']) == 4 and (2010 < int(data['Year']) < 2021):
                        print(j, end=" ")
                        print(data['Year'])
                        movies.setdefault(j, data['Year'])
                        movie_count = movie_count + 1

    else:
        print("Actor Not found!")
