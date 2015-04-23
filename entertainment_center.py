import fresh_tomatoes
import database
import media

# creates a list of movies from a sqlite database file 
movies = database.get_all_movies()

# creates a webpage to display the results
fresh_tomatoes.open_movies_page(movies)

