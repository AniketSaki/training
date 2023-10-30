import datetime
class MovieRating:
    # Static fields
    required_fields = ['Const','Your Rating', 'Date Rated', 'Title', 'URL', 'Title Type',
                      'IMDb Rating', 'Runtime (mins)', 'Year', 'Genres', 'Num Votes',
                      'Release Date', 'Directors']

    def __init__(self, const, your_rating, date_rated, title, url, title_type,
                 imdb_rating, runtime_mins, year, genres, num_votes, release_date, directors):
        self._const = const
        self._your_rating = your_rating
        self._date_rated = date_rated
        self._title = title
        self._url = url
        self._title_type = title_type
        self._imdb_rating = imdb_rating
        self._runtime_mins = runtime_mins
        self._year = year
        self._genres = genres
        self._num_votes = num_votes
        self._release_date = release_date
        self._directors = directors

    # Getters and setters
    def get_your_rating(self):
        return self._your_rating

    def set_your_rating(self, your_rating):
        self._your_rating = your_rating
        self._date_rated = self._get_current_date()

    def get_date_rated(self):
        return self._date_rated

    def set_date_rated(self, date_rated):
        self._date_rated = date_rated

    def _get_current_date(self):
        # Format the current date as 'MM-DD-YYYY'
       return datetime.datetime.now().strftime('%m-%d-%Y')
    
    def _get_title(self):
        return self._title
    
    def set_title(self, title):
        self._title = title

    def get_url(self):
        return self._url
    
    def set_url(self, url):
        self._url = url
    
    def get_title_type(self):
        return self._title_type
    
    def set_title_type(self, title_type):
        self._title_type = title_type
    
    def get_imdb_rating(self):
        return self._imdb_rating
    
    def set_imdb_title(self, imdb_title):
        self._imdb_title = imdb_title
    
    def get_runtime_mins(self):
        return self._runtime_mins
    
    def set_runtime_mins(self, runtime_mins):
        self._runtime_mins = runtime_mins

    def get_year(self):
        return self._year
    
    def set_year(self, year):
        self._year = year

    def get_genres(self):
        return self._genres
    
    def set_genres(self, genres):
        self._genres = genres

    def get_num_votes(self):
        return self._num_votes
    
    def set_num_votes(self, num_votes):
        self._num_votes = num_votes

    def get_release_date(self):
        return self._release_date
    
    def set_release_date(self, release_date):
        self._release_date = release_date

    def get_directors(self):
        return self._directors
    
    def set_directors(self, directors):
        self._directors = directors



movie_data = {
    'const': '12345',
    'your_rating': 8,
    'date_rated': '1-13-2023',
    'title': 'Sample Movie',
    'url': 'http://example.com/sample-movie',
    'title_type': 'Feature Film',
    'imdb_rating': 7.5,
    'runtime_mins': 120,
    'year': 2020,
    'genres': 'Drama',
    'num_votes': 1000,
    'release_date': '01-01-2021',
    'directors': 'John Doe'
}

movie_rating = MovieRating(**movie_data)

print(movie_rating)
print(f' Original Your Rating:{movie_rating.get_your_rating()}')
print(f'Original Date Rated: {movie_rating.get_date_rated()}')

# Update Your Rating
movie_rating.set_your_rating(9)
print(f'Updated Your Rating: {movie_rating.get_your_rating()}')
print(f'Updated Date Rated: {movie_rating.get_date_rated()}')
