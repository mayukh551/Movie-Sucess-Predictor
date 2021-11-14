import requests as r
import os

api_key = os.environ.get('MOVIE_API')

movie_name = input('Enter a name : ')
print()

# # &language=en-US

# To achieve movie details and movie ID using the following url

url = "https://api.themoviedb.org/3/search/movie?api_key=" + api_key + "&query=" + movie_name + "&page=1&include_adult=false"

response = r.get(url)
data = response.json()
movie_details = data['results']
movie_details = movie_details[0]
mov_id = movie_details['id']

# to fetch imdb id

url = "https://api.themoviedb.org/3/movie/" + str(mov_id) + "?api_key=" + api_key

response = r.get(url)
data = response.json()

imdb_id = data['imdb_id']

# to fetch ratings from diff sources using imdb_id
#
# url = "http://www.omdbapi.com/?apikey=c4779b30&i=" + str(imdb_id) + "&plot=full"
#
# response = r.get(url)
# data = response.json()
#
# for i, j in data.items():
#     print(i, ":", j)

# print(data)
# year = data['Year']
# runtime = data['Runtime']
# genre = data['Genre'].split(',')
# director = data['Director']
# cast = data['Actors'].split(',')
# print(year)
# print(*genre)
# print(director)
# print(*cast)
# print(data['imdbRating'])

# Movie Details

# print('Movie Name : ', movie_details['original_title'])
# print('Description : ')
# print(movie_details['overview'])
# print()
# print("Release date : ", movie_details['release_date'])
# print("Viewers' vote : ", movie_details['vote_average'])
#
#
# # To fetch Movie cast and crew details
#
# url = "https://api.themoviedb.org/3/movie/" + str(mov_id) + "/credits?api_key=" + api_key
#
# response = r.get(url)
# data = response.json()


# To find a actor or director details using person_id

# person_id = i['id']
# url = "https://api.themoviedb.org/3/person/" + str(person_id) + "?api_key=001a39241eb26389e5bcf5f8f4bfa764&language=en-US"
# response = r.get(url)
# per_info = response.json()
# print(per_info['popularity'])
