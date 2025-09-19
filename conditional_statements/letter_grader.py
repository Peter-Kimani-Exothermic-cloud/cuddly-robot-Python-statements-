#Letter grader with Nested if Statements

#We can even create a program that assigns letter grades based on a student’s score using nested if statements:

score = int ("Enter your score:")

if score >= 90:
    grade = "A"

elif score >= 80:
    grade = "B"

elif score >= 70:
    grade = "C"

else:
    grade = "F"


print(f"Your score is {grade} grade ")

#This program takes the student’s score as input. 
#It then uses a chain of if statements to check for specific score ranges and assigns the corresponding letter grade.