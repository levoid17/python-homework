user_phone_number = input("Enter your phone number: ")
if (
    len(user_phone_number) == 10
    and user_phone_number.isdigit()):
    match user_phone_number[:3]:
        case "050" | "051" | "055" | "070" | "077" | "099":
            print("Valid phone number.")
        case _:
            print("Invalid phone number.")