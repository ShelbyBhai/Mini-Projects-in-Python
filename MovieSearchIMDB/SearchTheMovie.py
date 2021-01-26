import imdb

hold = imdb.IMDb()

_movie_In_Search = input("Enter the Name of your desired Movie : ")

movies = hold.search_movie(_movie_In_Search)

_desired_movie = hold.get_movie(movies[0].getID())

print(_desired_movie['title'])

print(_desired_movie['year'])

_modified_cast = ','.join(map(str,_desired_movie['cast']))

print(_modified_cast)


