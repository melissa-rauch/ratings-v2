"""A file to seed database"""

import os
import json
from random import choice, randint
from datetime import datetime
import server
import model
import crud



os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

#Create movies, store them in a list so we can use them
#to create ratings later


movies_in_db = []
for movie in movie_data:

    #TODO: get the title, overview, and poster_path from the movie dictionary. 
    title, overview, poster_path = (movie['title'], 
                                    movie['overview'], 
                                    movie['poster_path'])
    #Then, get the release_date and convert it to a 
    #datetime object with datetime.strptime
    release_date = datetime.strptime(movie['release_date'],"%Y-%M-%d")

    #TODO: create a movie here and append it to movies_in_db

    db_movie = crud.create_movie(title, 
                                overview, 
                                release_date,
                                poster_path)

    movies_in_db.append(db_movie)

#create 10 users; each user will make 10 ratings
for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    user = crud.create_user(email,password)

    for _ in range(10):
        random_movie = choice(movies_in_db)
        score = randint(1,5)
        crud.create_rating(user,random_movie, score)

