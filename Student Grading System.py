student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermoine" : 99,
    "draco" : 74,
    "Nerville" : 62,
}

student_grade = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grade[student] = "Outstanding" 
    elif score > 80:
        student_grade[student] = "Exceeds Expectation" 
    elif score > 70:
        student_grade[student] = "Acceptable" 
    elif score > 60:
        student_grade[student] = "Poor"  
    else:
        student_grade[student] = "Fail"  

print(student_grade)
