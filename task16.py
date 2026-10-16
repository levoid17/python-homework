exam_score=int(input("Enter the student's exam score: "))
if exam_score<0 or exam_score>100:
    print("Invalid exam score.")
elif exam_score>=51:
    print("Passed.")
else:
    print("Failed.")