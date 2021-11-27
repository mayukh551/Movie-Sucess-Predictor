d = {'a': 1, 'b': 2}
print(len(d))

# import requests as r
#
# movie = input("Enter an movie name : ")
#
# # to fetch movie id
# url = "https://api.themoviedb.org/3/search/movie?api_key=001a39241eb26389e5bcf5f8f4bfa764&page=1&query=" + movie + "&include_adult=false"
# response = r.get(url)
# data = response.json()
#
# #  arraylist
# movie_data = data['results']
# z = 0
# #  i is element of movie_data representing a dict
# for i in movie_data:
#     if 'original_title' in i and i['original_title'] == movie:
#         z = i
#         break
#
# if z != 0:
#     movie_id = z['id']
#
#     #  to fetch the list of actors in the movie
#     url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "/credits?api_key=001a39241eb26389e5bcf5f8f4bfa764"
#
#     response = r.get(url)
#     data = response.json()
#     c = 0
#     cast = data['cast']
#     actors = []
#     for actor in cast:
#         if actor['known_for_department'] == 'Acting':
#             actors.append(actor['name'])
#             c = c + 1
#         if c == 6:
#             break
#
#     print(*actors)
# else:
#     print("Movie Not found")
#
