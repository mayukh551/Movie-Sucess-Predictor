# Movie-Success-Predictor

### **Members of this project :**
- Mayukh Bhowmick
- Rounak Hazra
- Abesh Biswas

### **Python Libraries** used for making this project :
- BeautifulSoap
- requests
- PIL (Python Imaging Library)
- Tkinter


<!-- <img src="C:\Users\MAYUKH\Desktop\project_SS.png"> -->
![Movie Success Predictor Desktop Application](https://github.com/mayukh551/Movie-Sucess-Predictor/blob/main/project_SS.png?)

### How does it work?
It asks for movie name from the user along with release year (optional)

Using Public API, we fetch:
- Release Year
- Cast List
- Director Name
- Movie Title
***
```Python
url = "http://www.omdbapi.com/?apikey=" + {api_key} + "&t=" + {Movie_Name} + "&y=" + {Release_Year} + "&plot=short"
response = requests.get(url)
movie_data = response.json()
```
From the cast list, top 5 cast are chosen and stored in a list : __(cast_list = [ ])__  

For every __actor/actress__ in __cast_list__ variable:  
- We check **IMDB** Ratings of at least 5 movies
performed by that actor/actress.  
- Store all the scores in list variable **score**.
- Extract best 3 scores from the score list and make an average  

After average score of every cast has been acquired,  
We choose the best **3 cast out of 5**

***

Using the same above process, we fetch the average rating of director

**best_actor_scores** : list of average scores of best 3 cast out of 5
```Python
p = gd = ok = flop = 0
print('Average imdb score of best 3 chosen out of 5 actors : ')
for i in best_actor_scores:
    print('%.2f' % i, end=" ")
    if 7.8 <= i:
        # p counts no. of good actors
        p = p + 1
    elif 7 < i < 7.8:
        gd = gd + 1
    elif 6 <= i <= 7:
        # ok counts no. of average actors
        ok = ok + 1
    elif i < 6:
        # flop counts no. of flop actors
        flop = flop + 1
```

The above code is used to a keep a track of :  

- No. of popular actors (p)  
- No. of good actors (gd)  
- No. of average actors (ok)  
- No. of flop actors (flop)
</br>

***

This data helps us to judge the movie based on cast _**popularity**_

```Python
dp = dok = dflop = 0
i = director_avg
if 7 <= i:
    dp =  1
elif 6 <= i < 7:
    dok = 1
else:
    dflop = 1
```
The above code is for judging the _**popularity**_ of director :  
- Popular / Good Director (dp)  
- Average Director (dok)  
- Flop Director (dflop)  
</br>

***

[OMDb API](https://www.omdbapi.com/) :  

For IMDB Rating, Release Year, Director Name, movie title  

[TMDB](https://developers.themoviedb.org/3/) :
- to extract cast list of the movie searched by the user
- To extract person_id and movie_id to get more info about them
- To extract the list of movies performed by a director


[IMDB](https://www.imdb.com/) :

  To extract the list of movies performed by an actor / actress  
  by webscraping IMDB website using BeautifulSoap


