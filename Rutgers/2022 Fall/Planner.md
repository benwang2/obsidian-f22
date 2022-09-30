<center> <h1>Rutgers University - Planner</h1> </center>


# Semester Overview

## Enrolled courses
- 01:198:210 - Data Management for Data Science
- 01:198:336 - Principles of Information and Data Management
- 01:198:352 - Internet Technology
- 01:960:401 - Basic Statistics for Research
- 01:988:101 - Introduction to Gender, Race, and Sexuality

# Tasks
## Recent work
```dataview
TABLE course as Course, file.mtime AS "Last modified"
FROM #lectureNotes
WHERE course != "CS_XXX"
SORT file.mtime DESC
LIMIT 5
```


# Schedule
### Assignments
```dataview
TABLE WITHOUT ID
	file.link as File, course as Course, due as "Due date"
FROM #Assignments 
WHERE date(due)+dur(1 day) > date(now)
SORT due ASC
LIMIT 4
```


### Relevant Dates
```dataview
TABLE WITHOUT ID
	course as Course, title as Title, due as Date
FROM csv("tables/relevant_dates.csv")
WHERE date(now)-dur(1 day) < date(due)
SORT due ASC
LIMIT 10
```
