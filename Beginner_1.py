'''Create a program that calculates the grade for a student based on their exam score,
using a grading scale with multiple ranges'''
def grader ():
    exam_score = float(input('Enter Exam Score: '))
    if exam_score > 89 and exam_score <= 100:
        grade = 'A'
    elif exam_score > 79 and exam_score <= 89:
        grade = 'B'
    elif exam_score > 69 and exam_score <= 79:
        grade = 'C'
    elif exam_score > 59 and exam_score <= 69:
        grade = 'D'
    elif exam_score >= 0 and exam_score <= 59:
        grade = 'F'
    
    else:
        grade = grader ()
        
    return grade

print (grader())