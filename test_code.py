d = {}
actor_hist = {}
d.setdefault('b', 5)
print(d)
actor_hist.setdefault('a', d)
print(actor_hist)

# {'a': {'b': 5}}

# from bs4 import BeautifulSoup
# import requests
#
# url ="https://www.imdb.com/chart/top/"
#
# try:
#     source = requests.get(url)
#     source.raise_for_status()
#     soup = BeautifulSoup(source.text, 'html.parser')
#     print(soup)
#
# except Exception as e:
#     print(e)
#
