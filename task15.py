#university admission algorithm
student_exam_score = float(input("Enter the student's exam score: "))
student_age = int(input("Enter the student's age: "))
student_school_score = float(input("Enter the student's school score: "))
if student_exam_score < 0 or student_exam_score > 700:
    print("Invalid exam score.")
if student_age < 0:
    print("Invalid age.")
if student_school_score < 0 or student_school_score > 100:
    print("Invalid school score.")
if student_age >= 16:
    if student_exam_score >= 600:
        print("The student is eligible for the scholarship and accepted.")
    elif student_exam_score >= 450 :
        print("The student is accepted.")
    elif student_exam_score >= 300 and student_school_score >= 80:
        print("The student is accepted.")
    else:
        print("The student is not accepted.")