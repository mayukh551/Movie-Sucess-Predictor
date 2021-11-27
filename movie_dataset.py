# Using web scraping to find
# last 5 movies performed by an actor or director

# from openpyxl import workbook, load_workbook
from bs4 import BeautifulSoup
import requests as r
import time

# wb = load_workbook('constituents3.xlsx')
# ws = wb.active
start = time.time()
person = input()
url = 'https://api.themoviedb.org/3/search/person?api_key=001a39241eb26389e5bcf5f8f4bfa764&query=' + person + '&language=en-US&page=1&include_adult=false'
response = r.get(url)
data = response.json()
cast_data = data['results']
person_id = ''
for i in cast_data:
    person_id = i['id']
    break
end = time.time()
print(f'Time taken by tmdb api call #1 and retrieving = {end - start}')
if person_id != '':
    start = time.time()
    url = 'https://api.themoviedb.org/3/person/' + str(
        person_id) + '?api_key=001a39241eb26389e5bcf5f8f4bfa764&language=en-US'
    response = r.get(url)
    data = response.json()
    # actor_imdb_id = 'nm4043618'
    actor_imdb_id = data['imdb_id']
    end = time.time()
    print(f'Time taken by tmdb api call #2 and retrieving = {end - start}')
    start = time.time()
    url = 'https://www.imdb.com/name/' + actor_imdb_id + '/?ref_=fn_al_nm_1'
    source = r.get(url)
    if source.status_code == 200:
        soup = BeautifulSoup(source.text, 'html.parser')
        l = soup.find('div', class_="filmo-category-section").find_all('div')
        end = time.time()
        print(f'Time taken by web scraping and retrieving = {end - start}')
        t = 0
        # terms = ['completed', 'post-production', 'pre-production', 'filming']
        for i in l:
            start = time.time()
            # print(i)
            # print(i.find('span').text[2:-1])
            if i.find('span').text != '':
                if '2012' < i.find('span').text[2:-1] < '2021':
                    print(i.find('b').a.text)
                    print()
            end = time.time()
            t = t + (end - start)
        print(f'Time taken by for loop = {t}')
else:
    print('Actor Not Found!')

# ws['A1'] = 'Movie'
#
# url = 'https://www.imdb.com/chart/top'
# i = 2
# source = r.get(url)
# if source.status_code == 200:
#     print('working\n')
#     soup = BeautifulSoup(source.text, 'html.parser')
#     movies = soup.find('tbody', class_="lister-list").find_all('tr')
#     for movie in movies:
#         rank = movie.find('td', class_="titleColumn").get_text
#         name = movie.find('td', class_="titleColumn").a.text
#         movie_name = 'A' + str(i)
#         ws[movie_name] = name
#         i = i + 1
#         # print(name)
#
# wb.save('constituents3.xlsx')

# movie_name = 'A' + str(2)
# i = 2
# while ws[movie_name].value is not None:
#     print(ws[movie_name].value)
#     i = i + 1
#     movie_name = 'A' + str(i)
