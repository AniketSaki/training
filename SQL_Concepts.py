import psycopg2
import csv
from datetime import datetime
import json

def convert_to_float(value):

    try:
        return float(value.strip("/").strip("'"))
    except ValueError as ve:
        return None  

def convert_to_string(value):
    return value.strip("/").strip("'").strip(",")

def convert_date_format(date_str):
    if date_str:
        date_object = datetime.strptime(date_str, '%m/%d/%Y')
        return date_object.strftime('%Y/%m/%d')
    else:
        return None
def convert_to_integer(value):
    if value:
        return int(value)
    else:
        return None

class PostgresCRUD:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.conn.cursor()

    def create_table(self):
        create_table_query = ("""
        CREATE TABLE IF NOT EXISTS ratings (
            "Const" VARCHAR(255) PRIMARY KEY,
            "Your_Rating" DOUBLE PRECISION,
            "Date_Rated" DATE,
            "Title" VARCHAR(255),
            "URL" VARCHAR(255),
            "Title_Type" VARCHAR(255),
            "IMDb_Rating" DOUBLE PRECISION,
            "Runtime_Mins" INTEGER,
            "Year" INTEGER,
            "Genres" VARCHAR(255),
            "Num_Votes" INTEGER,
            "Release_Date" DATE,
            "Directors" VARCHAR(255)
        );
        """)
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def insert_data_from_csv(self, csv_file):
        with open(csv_file, encoding='latin-1') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                genres = convert_to_string(row['Genres'])
                directors = convert_to_string(row['Directors'])
                date_rated = convert_date_format(row['Date Rated'])
                release_date = convert_date_format(row['Release Date'])
                your_rating = convert_to_float(row['Your Rating'])
                imdb_rating = convert_to_float(row['IMDb Rating'])
                runtime_mins = convert_to_integer(row['Runtime (mins)'])
               
                insert_query = """
                INSERT INTO ratings 
                ("Const", "Your_Rating", "Date Rated", "Title", "URL", "Title_Type", "IMDb_Rating", "Runtime_mins", "Year", "Genres", "Num_Votes", "Release_Date", "Directors") 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT ("Const") DO UPDATE
                SET
                    "Your_Rating" = EXCLUDED."Your_Rating",
                    "Date Rated" = EXCLUDED."Date Rated",
                    "Title" = EXCLUDED."Title",
                    "URL" = EXCLUDED."URL",
                    "Title_Type" = EXCLUDED."Title_Type",
                    "IMDb_Rating" = EXCLUDED."IMDb_Rating",   
                    "Runtime_mins" = EXCLUDED."Runtime_mins",
                    "Year" = EXCLUDED."Year",
                    "Genres" = EXCLUDED."Genres",
                    "Num_Votes" = EXCLUDED."Num_Votes",
                    "Release_Date" = EXCLUDED."Release_Date",
                    "Directors" = EXCLUDED."Directors";
                """
                table_data = (
                    row['Const'], your_rating, date_rated, row['Title'], row['URL'], row['Title Type'],
                    imdb_rating, runtime_mins, row['Year'], genres, row['Num Votes'], release_date, directors)
                self.cursor.execute(insert_query, table_data)
                self.conn.commit()

    def list_total_records(self):
        query = "SELECT COUNT(*) FROM ratings;"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def list_records_by_title_type(self):
        query = "SELECT \"Title_Type\", COUNT(*) FROM ratings GROUP BY \"Title_Type\";"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def list_records_by_year_rating(self):
        query = "SELECT EXTRACT(YEAR FROM \"Date Rated\") AS rating_year, COUNT(*) FROM ratings GROUP BY rating_year ORDER BY rating_year;"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def list_record_by_top_10_rated_titles(self):
        query = "SELECT \"Title\", \"IMDb_Rating\" FROM ratings ORDER BY \"IMDb_Rating\" DESC LIMIT 10;"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def list_record_by_bottom_10_rated_titles(self):
        query = "SELECT \"Title\", \"IMDb_Rating\" FROM ratings ORDER BY \"IMDb_Rating\" ASC LIMIT 10;"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def list_record_by_genres_average_ratings(self):
        query = "SELECT unnest(string_to_array(\"Genres\", ', ')) AS genre, AVG(\"IMDb_Rating\") AS average_rating FROM ratings GROUP BY genre ORDER BY average_rating DESC;"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def fetch_records_in_ratings_histogram(self):
        query = "SELECT width_bucket(\"IMDb_Rating\", 0, 10, 10) AS bucket, COUNT(*) FROM ratings GROUP BY bucket ORDER BY bucket;"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def generate_json_queries(self, filename):
        queries = {
            "total_records": "SELECT COUNT(*) FROM ratings;",
            "records_by_Title_Type": "SELECT \"Title_Type\", COUNT(*) FROM ratings GROUP BY \"Title_Type\";",
            "records_by_year_of_rating": "SELECT EXTRACT(YEAR FROM \"Date Rated\") AS rating_year, COUNT(*) FROM ratings GROUP BY rating_year ORDER BY rating_year;",
            "records_by_year_of_release": "SELECT EXTRACT(YEAR FROM \"Release_Date\") AS release_year, COUNT(*) FROM ratings GROUP BY release_year ORDER BY release_year;",
            "top_10_rated_titles": "SELECT \"Title\", \"IMDb_Rating\" FROM ratings ORDER BY \"IMDb_Rating\" DESC LIMIT 10;",
            "bottom_10_rated_titles": "SELECT \"Title\", \"IMDb_Rating\" FROM ratings ORDER BY \"IMDb_Rating\" ASC LIMIT 10;",
            "genres_average_ratings": "SELECT unnest(string_to_array(\"Genres\", ', ')) AS genre, AVG(\"IMDb_Rating\") AS average_rating FROM ratings GROUP BY genre ORDER BY average_rating DESC;",
            "ratings_histogram": "SELECT width_bucket(\"IMDb_Rating\", 0, 10, 10) AS bucket, COUNT(*) FROM ratings GROUP BY bucket ORDER BY bucket;",
        }
        
        with open(filename, 'w') as json_file:
            json.dump(queries, json_file, indent=4)
            
    def execute_queries_from_json(self,filename):
        with open(filename, 'r') as json_file:
            queries = json.load(json_file)
        results = {}
        for query_name, query in queries.items():
            self.cursor.execute(query)
            results[query_name] = self.cursor.fetchall()
        return results
    def close_connection(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    db = PostgresCRUD(
        dbname='postgres',
        user='postgres',
        password='Aishwarya@07',
        host='localhost',
        port='5432'
    )
    db.create_table()
    db.insert_data_from_csv("ratings.csv")
    db.generate_json_queries("queries.json")
    results = db.execute_queries_from_json("queries.json")
    print(results)
    db.close_connection()
    
    
