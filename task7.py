user_age=int(input("Enter your age: "))
if user_age < 0:
    print("Invalid age. Please enter a non-negative number.")
else:
    if user_age < 13:
        print("You are a child.")
    elif user_age < 20:
        print("You are a teenager.")
    elif user_age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")