<center> <h1>Rutgers University - Planner</h1> </center>


# Classes
- 01:198:210 - Data Management for Data Science
- 01:198:336 - Principles of Information and Data Management
- 01:198:352 - Internet Technology
- 01:960:401 - Basic Statistics for Research
- 01:988:101 - Introduction to Gender, Race, and Sexuality

# Schedule

## Relevant Dates
```dataview
TABLE
	course, title, date, time
FROM csv("relevant_dates.csv")
SORT due DESC
```








## Assignments
```dataview
TABLE
	title, course, due
FROM #Assignments 
WHERE date(due) > date(now)
SORT due DESC
```
