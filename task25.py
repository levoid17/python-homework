student_id=input("Enter the student ID: ")
student_age=int(input("Enter the student age: "))
workshop_code=input("Enter the workshop code: ").upper()
if len(student_id)==8 and student_id.isdigit:
    if student_age >= 16 and student_age <= 65:
        match workshop_code:
            case "PY":
                payment=30
                if student_age >= 16 and student_age <=18:
                    payment=payment*0.8
                    print (f"you are eligible to study payment amount will be {payment:.2f} AZN")
                else :
                    print (f"you are eligible to study payment amount will be {payment:.2f} AZN")
            case "WEB":    
                payment=40
                if student_age >= 16 and student_age <=18:
                    payment=payment*0.8
                    print (f"you are eligible to study payment amount will be {payment:.2f} AZN")
                else:
                    print (f"you are eligible to study payment amount will be {payment:.2f} AZN")

            case "CY":
                payment=50
                if student_age > 18:
                    print (f"you are eligible to study payment amount will be {payment:.2f} AZN")
                elif student_age == 18:
                    payment=payment*0.8
                    print (f"you are eligible to study payment amount will be {payment:.2f} AZN")
                else:
                    print("You are not elligible for studying")
    else:
        print('You are not allowed to study at this age')
else:
    ('Wrong student ID')