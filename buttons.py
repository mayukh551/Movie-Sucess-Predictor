import requests as r

movie = input("Enter a movie name : ")
year = input("Enter the year of release : ")

if len(year) == 4:
    url = "http://www.omdbapi.com/?apikey=c4779b30&t=" + movie + "&y=" + year + "&plot=full&type=movie"
else:
    url = "http://www.omdbapi.com/?apikey=c4779b30&t=" + movie + "&plot=short"

response = r.get(url)
data = response.json()
# if 'not found' in data['Error']:
#     print("Movie Not Found!")
# else:
print(data)
year = data['Year']
runtime = data['Runtime']
genre = data['Genre'].split(',')
director = data['Director']
cast = data['Actors'].split(',')
print(year)
print(*genre)
print(director)
print(*cast)
print(data['imdbRating'])
