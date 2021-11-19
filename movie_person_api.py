# To fetch actors list from a specific movie
# using TMDB API

import requests as r


def findCast(movie, year):
    # movie = input("Enter an movie name : ")
    print('file-3')
    url = "https://api.themoviedb.org/3/search/movie?api_key=001a39241eb26389e5bcf5f8f4bfa764&page=1&query=" + movie + "&include_adult=false&year=" + str(
        year)

    # url = 'https://api.themoviedb.org/3/search/movie?api_key=001a39241eb26389e5bcf5f8f4bfa764&query=PK&page=1&include_adult=false'
    response = r.get(url)
    data = response.json()

    movie_data = data['results']
    # Grabbing the dictionary where movie id is present
    z = 0
    #  i is element of movie_data representing a dict
    for i in movie_data:
        # print(i)
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
        for actor in cast:
            if actor['known_for_department'] == 'Acting':
                actors.append(actor['name'])
                c = c + 1
            if c == 5:
                break
        return actors

    else:
        print("Movie Not found")
        return 0


# print(*findCast(input('Enter movie name : '), int(input('Enter release year : '))))

# known_for_department

# d = data['results']
# person_id = d[0]['id']
# print("person_id", person_id)
# print(d)
# for j in d:
#     print(j)
# print()
# mov_list = []
# for j in d:
#     for i in range(0, 3):
#         mov_list.append(j['known_for'][i]['original_title'])
#         print(j['known_for'][i]['original_title'])
#
# rating_sum = 0
