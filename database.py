import sqlite3 as lite
import sys
import media
    
def get_all_movies():
	''' return a list of moves from a database file "moves.db" '''
	con =lite.connect('movies.db')
	all_movies = []
	
	with con:
		cur= con.cursor()
		cur.execute("SELECT title, storyline, image_url, trailer_url FROM Movies")
		
		rows = cur.fetchall()
		for row in rows:
			all_movies.append(media.Movie(row[0], row[1], row[2], row[3]))
	
	return all_movies
#get_all_movies()