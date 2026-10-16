user_age=int(input("Enter your age: "))
user_salary=float(input("Enter your salary: "))
user_loan_amount=float(input("Enter your loan amount: "))
if (user_age < 0):
    print("Invalid age.")
elif user_salary < 0:   
    print("Invalid salary.")
elif user_loan_amount < 0:
    print("Invalid loan amount.")
if user_age >= 18:
    if user_salary >= 500:
        if user_loan_amount <= 10*user_salary:
            print("You are eligible for the loan.")
        else:
            print("You are not eligible for the loan due to high loan amount.")
    else:
        print("You are not eligible for the loan due to low salary.")
else:
    print("You are not eligible for the loan due to age.")