from openpyxl import workbook, load_workbook
from bs4 import BeautifulSoup
import requests as r

wb = load_workbook('constituents3.xlsx')
ws = wb.active


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

movie_name = 'A' + str(2)
i = 2
while ws[movie_name].value is not None:
    print(ws[movie_name].value)
    i = i + 1
    movie_name = 'A' + str(i)
