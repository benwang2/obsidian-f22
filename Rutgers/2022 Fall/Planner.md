<center> <h1>Rutgers University - Planner</h1> </center>


# Semester Overview

## Enrolled courses
- 01:198:210 - Data Management for Data Science
- 01:198:336 - Principles of Information and Data Management
- 01:198:352 - Internet Technology
- 01:960:401 - Basic Statistics for Research
- 01:988:101 - Introduction to Gender, Race, and Sexuality

# Schedule
### Assignments
```dataview
TABLE WITHOUT ID
	file.link as assignment, course, due
FROM #Assignments 
WHERE date(due) > date(now)
SORT due DESC
LIMIT 4
```

### Relevant Dates
```dataview
TABLE WITHOUT ID
	course, title, due as date
FROM csv("tables/relevant_dates.csv")
WHERE date(due) > date(now)
SORT due ASC
LIMIT 10
```


















