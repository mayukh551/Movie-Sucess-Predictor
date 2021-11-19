# This code is for retrieving
# all cast names of a movie


# importing the module
import imdb


def findCast(name, y):
    print('file-3')
    # creating instance of IMDb
    ia = imdb.IMDb()
    # name = input("Enter a movie name : ")
    # y = int(input("Year of release"))
    search = ia.search_movie(name)
    # print(search)
    cond = False
    # loop for printing the name and id
    for i in range(len(search)):
        # getting the id
        print(search[i]['title'], search[i]['year'])
        id = search[i].movieID
        if search[i]['title'] == name and str(search[i]['year']) == y:
            cond = True
            break
        # printing it
        # print(search[i]['title'], " : ", id)
    if cond:
        print("Movie Found")
    else:
        print("Movie Not Found")
        return 0

    code = id
    # getting movie
    movie = ia.get_movie(code)
    # getting cast
    cast = movie['cast']
    actor_list = []
    for i in cast:
        actor_list.append(i['name'])
        # print(i['name'], end=" ")
    print()
    return actor_list
