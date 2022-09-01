# This repo is for training on Python.

## Introduction
The data folder contains a ratings.csv file. The file has the following columns:
Const,Your Rating,Date Rated,Title,URL,Title Type,IMDb Rating,Runtime (mins),Year,Genres,Num Votes,Release Date,Directors

## OOP Concepts via Class
1) Create a Class with the above listed properties. 
   - The required fields should be listed static.
   - There should be get and set methods.
   - There should be a function to update Your Rating.
   - Updating Your Rating should also update Date Rated internally.
2) Programatically read the CSV file
3) Iterate through the contents of the CSV file and for each row
4) Create a new instance of above class. 
## SQL Concepts 
5) Download PostgreSQL DB and create a workspace and table
6) Create a class to interact with Postgres. Basic CRUD functionality
7) Insert all rows into DB using class instance 
8) Create a JSON file with SQL commands for the following cases:
   - List total number of records in table.
   - List number of records by title type, i.e. Movie, TV, etc.
   - List number of records by year of rating.
   - List number of records by year of release.
   - List number of records by country of origin.
   - List number of records by language.
   - List the top 10 rated titles.
   - List the bottom 10 rated titles.
   - List genres by their average ratings, sorted decrementally.
   - Fetch histogram of ratings.
9) Read the JSON file and execute all Read queries.
10) Update the rating when given a title.
11) Delete the rating when given a title.
## Pandas API
12) Execute the above Read queries using Pandas API.
## Spark SQL
13) Execute the above Read queries using PySpark SQL.

###########################################

* Create a virtual environment
* Create a requirements.txt file with required dependencies
* Create a .gitignore file
* Add docstrings to all files
* Create a Unit test case
* Generate test coverage

###########################################

* Clone the repository to your own
* Create a new branch
* Every commit should be GPG signed
* Create a Pull Request with updated code
