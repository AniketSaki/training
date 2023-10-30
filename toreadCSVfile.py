import ast
import csv
from Python_OOPS import MovieRating

file_path = 'ratings.csv'

def convert_to_float(value):
    try:
        return float(value.strip("/").strip("'"))
    except ValueError as ve:
        print(ve.args)
        return None

def read_movie_ratings_from_csv(file_path):
    movie_ratings = []  
    with open(file_path, 'r', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
 
        for row in reader: 
            imdb_rating = convert_to_float(row['IMDb Rating'])
            try:
                if all(field in row for field in MovieRating.required_fields):
                    movie_rating = MovieRating(
                        row['Const'],int(row['Your Rating']),row['Date Rated'],
                        row['Title'], row['URL'], row['Title Type'],
                        imdb_rating, int(row['Runtime (mins)']), int(row['Year']), row['Genres'],
                        int(row['Num Votes']), row['Release Date'], row['Directors']
                    )
                    movie_ratings.append(movie_rating)
            except ValueError:
                pass
            except KeyError as ke:
                print(ke.args)
                pass

    return movie_ratings

movie_ratings_list = read_movie_ratings_from_csv(file_path)

for movie_rating in movie_ratings_list:
    print(f"Movie Title: {movie_rating. _get_title()}, Your Rating: {movie_rating.get_your_rating()}, Date Rated: {movie_rating._date_rated}, IMDb rating:{movie_rating.get_imdb_rating()}")
