import requests as r
from datetime import date
import time

# Colin Farrell
person = input("Enter actor's name : ")
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
    start = time.time()
    arranged_movies_list = sorted(lis, key=lambda x: x['release_date'], reverse=True)
    end = time.time()
    print(f'Time taken : {end - start}')
    start = time.time()
    final_year = []
    final_lis = []
    for i in lis:
        final_year.append(int(i['release_date'][:4]))
        final_lis.append(i['original_title'])

        # print(i)
        # print('\n')

    earliest_year = min(final_year)
    for i in final_year:



    if i['release_date'][:4] > final_year[0][:4]:
        print(i['original_title'], i['release_date'])
        final_year.insert(0, i['release_date'])
        final_lis.insert(0, i['original_title'])

    end = time.time()
    print(f'Time taken : {end - start}')
    for i, j in zip(final_lis, final_year):
        print(i, j)

    # try:
    #     arranged_movies_list = sorted(lis, key=lambda x: x['release_date'], reverse=True)
    # except KeyError:
    #     arranged_movies_list = lis

# import requests as r
# from datetime import date
#
# person = input('Enter person name : ')
#
# url = 'https://api.themoviedb.org/3/search/person?api_key=001a39241eb26389e5bcf5f8f4bfa764&query=' + person + '&language=en-US&page=1&include_adult=false'
# response = r.get(url)
# data = response.json()
# cast_data = data['results']
# person_id = ''
# for i in cast_data:
#     person_id = i['id']
#     break
#
# # if person_id not empty
# if person_id != '':
#     # print(person, ':', person_id)
#     # to fetch the list of movies performed by the user
#     url = 'https://api.themoviedb.org/3/discover/movie?api_key=001a39241eb26389e5bcf5f8f4bfa764&language=en-US&with_cast=' + str(
#         person_id) + '&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate'
#     response = r.get(url)
#     data = response.json()
#     # for i in data['results']:
#     #     print(sorted(i))
#     lis = data['results']
#     arranged_movies_list = sorted(lis, key=lambda x: x['release_date'], reverse=True)
#     final_movie_list = []
#
#     for item in arranged_movies_list:
#         today = str(date.today())
#         yor = item['release_date']
#         if yor <= today[:4] and ((yor[5:7] <= today[5:7]) or (yor[8:] <= today[8:])):
#             print(item['original_title'], end=" ")
#             print(yor)
#             final_movie_list.append(item['original_title'])
#             if len(final_movie_list) == 5:
#                 break
#     print()
#     for k in final_movie_list:
#         print(k)


# d = {1: 'a', 2: 'b', 3: 'c'}
# print(d[4])
