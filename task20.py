student_id = input("Enter your student ID: ")
if len(student_id) == 8:
    a = int(student_id)
    if bool(a):
            print("Valid student ID.")
    else:
            print("Invalid student ID.")
else:
    print("Invalid student ID.")