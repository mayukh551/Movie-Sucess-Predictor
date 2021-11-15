import requests as r

# to fetch movie names following person is involved

movie = input("Enter an movie name : ")
# movie = 'Avengers: Endgame'
# original_title

url = "https://api.themoviedb.org/3/search/movie?api_key=001a39241eb26389e5bcf5f8f4bfa764&page=1&query=" + movie + "&include_adult=false"

# url = 'https://api.themoviedb.org/3/search/movie?api_key=001a39241eb26389e5bcf5f8f4bfa764&query=PK&page=1&include_adult=false'
response = r.get(url)
data = response.json()

#  arraylist
movie_data = data['results']
# print(movie_data)
z = 0
#  i is element of movie_data representing a dict
for i in movie_data:
    # print(i)
    if 'original_title' in i and i['original_title'] == movie:
        z = i
        break

# print(z)
if z != 0:
    movie_id = z['id']

    url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "/credits?api_key=001a39241eb26389e5bcf5f8f4bfa764"

    response = r.get(url)
    data = response.json()
    c = 0
    cast = data['cast']
    actors = []
    for actor in cast:
        if actor['known_for_department'] == 'Acting':
            actors.append(actor['name'])
            c = c + 1
        if c == 6:
            break

    print(*actors)
else:
    print("You r fucked")
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
