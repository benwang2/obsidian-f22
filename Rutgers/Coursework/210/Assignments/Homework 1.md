---
title: Homework 1
course: CS210
released: 2022/09/26
due: 2022/10/07
---
<center><h1>Homework 1</h1></center>

<center><h3>CS210 Data Management for Data Science</h3></center>

## Overview
In this assignment, you’ll implement a prototype movie recommendation program in Python according to the following guidelines. You can work individually or in a group of up to 4 people.

## What to Submit
Write all the required functions described below in the given template file named hw1.py, and submit your completed hw1.py. If you are working in a group, only one person should submit, and your hw1.py file should have a comment that gives the names and netIDs of everyone in your group.
You can resubmit any number of times. The last submission will be graded. 
You may also implement other helper functions as needed. Make sure you write all your test calls  
in the main() function. Do not write any code outside of any of the functions. We’ll ignore your  
main() function when grading.

## How to test your code  
You can test your program by calling your functions in the hw1.py file. All test code must be in the main() function. 

Make sure the test files are in the same folder as the program. You may develop and test your code in a Jupyter notebook, but for submission you will need to move your code over to hw1.py and execute it as above to make sure it works correctly. 

You can run your tests on the given ratings and movies files, but testing on only these files may not be sufficient. You should make your own test files as well, to make sure that you cover the various paths of logic in your functions. You are not required to submit any of your test files.  

You may assume that all parameter values given to your functions will be valid. Also, in any function that requires the returned values to be sorted or ranked, ties may be broken arbitrarily  
between equal values.

## Data Input
- Ratings file: A text file that contains movie ratings. Each line has the name (with year) of a movie, its rating (range 0-5 inclusive), and the id of the user who rated the movie. A movie can have multiple ratings from different users. A user can rate multiple movies, but can rate a particular movie only once.  

- Movies file: A text file that contains the genres of movies. Each line has a genre, a movie id, and the name (with year) of the movie. To keep it simple, each movie belongs to a single genre. Note: A movie name includes the year to disambiguate movies with the same title. 

There are sample movies and ratings files provided on Canvas.

You may assume that input files will be correctly formatted, and data types will be as expected. For all rating computations, do not round up (or otherwise modify) the rating unless otherwise specified.

## Task 1: Reading Data
(8 points) Movie ratings  
Write a function read_ratings_data(f) that takes in a ratings file name, and returns a dictionary.  
The dictionary should have movie as key, and the corresponding list of ratings as value.  
For example:  
{  
"The Lion King (2019)": [6.0, 7.5, 5.1],  
"Titanic (1997)": [7]  
}

#Assignments 