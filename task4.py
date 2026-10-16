exam_score=int(input("Enter your exam score: "))
if exam_score < 0 or exam_score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
else:
    match exam_score:
        case score if score >= 91: print("Grade: A")
        case score if score >= 81: print("Grade: B")
        case score if score >= 71: print("Grade: C")
        case score if score >= 61: print("Grade: D")
        case score if score >= 51: print("Grade: E")
        case _: print("Grade: F")