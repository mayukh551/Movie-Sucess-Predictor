runtime = "175 min"
runtime = runtime[:runtime.find('m') - 1]
print(runtime)
print(int(runtime) > 75)

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
