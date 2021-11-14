import requests as r

# to fetch movie names following person is involved

person = input("Enter an actor's name : ")


url = "https://api.themoviedb.org/3/search/person?api_key=001a39241eb26389e5bcf5f8f4bfa764&page=1&query=" + person + "&include_adult=false"

response = r.get(url)
data = response.json()

# pop_list = data['results'][0]['popularity']

# print(pop_list)
# print()
# knownFor = data['results'][0]['known_for']
# print(knownFor)

d = data['results']
person_id = d[0]['id']
print("person_id", person_id)
print(d)
for j in d:
    print(j)
print()
mov_list = []
for j in d:
    for i in range(0, 3):
        mov_list.append(j['known_for'][i]['original_title'])
        print(j['known_for'][i]['original_title'])

rating_sum = 0

for movie in mov_list:
    url = "http://www.omdbapi.com/?apikey=c4779b30&t=" + movie + "&plot=full"
    response = r.get(url)
    data = response.json()
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
    rating_sum = rating_sum + float(data['imdbRating'])
    print()

rating_avg = rating_sum/(len(mov_list))

print(f'Average rating : {rating_avg}')

