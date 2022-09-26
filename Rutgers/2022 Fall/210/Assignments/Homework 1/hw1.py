import math
from collections import defaultdict
from collections import Counter

# You may not add any other imports

# For each function, replace "pass" with your code

# --- TASK 1: READING DATA ---

# 1.1
def read_ratings_data(f):
    """Takes in a ratings file name, and returns a dictionary. The dictionary has the movie as a key, and the corresponding list of ratings as value."""
    data = {}

    with open(f,"r") as file:
        lines = file.readlines()
        for line in lines:
            title, rating, _id = line.strip().split("|")
            if title not in data:
                data[title] = []

            data[title].append(float(rating))

    return data

# 1.2
def read_movie_genre(f):
    """Takes in a movies file name and returns a dictionary mapping each movie to it's corresponding genre.
    """
    data = {}

    with open(f,"r") as file:
        lines = file.readlines()
        for line in lines:
            genre, _, title = line.strip().split("|")
            data[title] = genre

    return data

# --- TASK 2: PROCESSING DATA ---

# 2.1
def create_genre_dict(d):
    data = {}

    for (k,v) in d.items():
        if v not in data:
            data[v] = []
        data[v].append(k)

    return data

# 2.2
def calculate_average_rating(d):
    return {k:round(sum(v)/len(v),1) for (k,v) in d.items()}

# --- TASK 3: RECOMMENDATION ---

# 3.1
def get_popular_movies(d, n=10):
    ordered = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return {item[0]:item[1] for item in ordered[:min(n,len(ordered))]}

# 3.2
def filter_movies(d, thres_rating=3):
    return {k:v for (k,v) in d.items() if v >= thres_rating}

# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    movies = filter(lambda item: item[1]==genre, genre_to_movies.items())
    movies = {x[0]:x[1] for x in movies}

    ratings = filter(lambda item: item[0] in movies, movie_to_average_rating.items())
    ordered = sorted(ratings, key=lambda x: x[1], reverse=True)

    return {item[0]:item[1] for item in ordered[:min(n,len(movies))]}
    

# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    movies = filter(lambda item: item[1]==genre, genre_to_movies.items())
    movies = {x[0]:x[1] for x in movies}

    movie_rating_tuples = filter(lambda item: item[0] in movies, movie_to_average_rating.items())
    
    avg = num_ratings = 0
    for (_, ratings) in movie_rating_tuples:
        avg += sum(ratings)
        num_ratings += len(ratings)
    
    return round(avg/num_ratings,1)

# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    genres = set([x[1] for x in genre_to_movies.items()])
    rated_genres = {genre:get_genre_rating(genre, genre_to_movies, movie_to_average_rating) for genre in genres}
    sorted_genres_by_rating = sorted(rated_genres.items(), key=lambda x: x[1], reverse=True)

    return {k:v for (k,v) in sorted_genres_by_rating[:min(n,len(sorted_genres_by_rating))]}

# --- TASK 4: USER FOCUSED ---

# 4.1
def read_user_ratings(f):
    data = {}

    with open(f,"r") as file:
        lines = file.readlines()
        for line in lines:
            title, rating, user_id = line.strip().split("|")
            if user_id not in data:
                data[user_id] = []

            data[user_id].append((title, float(rating)))

    return data

# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    users_ratings = user_to_movies[user_id]
    users_rated_genres = {}

    for (movie, rating) in users_ratings:
        genre = movie_to_genre[movie]
        if not genre in users_rated_genres:
            users_rated_genres[genre] = []
        users_rated_genres[genre].append(rating)

    top_genre = None
    max_rating = 0
    for (genre, ratings) in users_rated_genres.items():
        if sum(ratings) > max_rating:
            max_rating = sum(ratings)
            top_genre = genre
    
    return top_genre

# 4.3
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    user_genre = get_user_genre(user_id, user_to_movies, movie_to_genre)

    rated_movies = {k[0]:True for k in user_to_movies[user_id]} 
    movies_in_genre = filter(lambda x: x[1] == user_genre and x[0] not in rated_movies, movie_to_genre.items())
    in_genre_by_rating = {k:movie_to_average_rating[k] for (k,_) in movies_in_genre}
    top_in_genre = sorted(in_genre_by_rating, key=lambda x: x[1], reverse=True)

    return top_in_genre[:min(3, len(top_in_genre))]


# --- main function for your testing ---
def main():
    pass

    

main()