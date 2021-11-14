# importing the module
import imdb
import requests as r

# creating instance of IMDb
ia = imdb.IMDb()

name = input("Enter actor's name : ")

# searching the name
search = ia.search_person(name)
country = 'India'


# to extract actor detail list
def extract_person_info(actor_results):
    for x, y in actor_results.items():
        if 'birth info' in actor_results['data'] and country in actor_results['data']['birth info']['birth place']:
            print(actor_results)
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

    movies = []

    #  list of movies performed by the actor/director/writer
    for j in info['filmography'][role]:

        #  To fetch year of release from omdb api

        url = "http://www.omdbapi.com/?apikey=c4779b30&t=" + str(j) + "&plot=full"
        response = r.get(url)
        data = response.json()
        if 'Year' in data:

            if len(data['Year']) == 4 and (2010 < int(data['Year']) < 2021):
                print(j, end=" ")
                print(data['Year'])
                movies.append(j)

else:
    print("Actor Not found!")

# mov_names = ia.search_movie('3 idiots')
# print(mov_names)
# print('2009' in mov_names[0])
