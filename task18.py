#day planner
weekdays = int(input("Enter the number of days (1-7): "))
match weekdays:
        case 1 | 2 | 3 | 4 | 5:
            print("It's a study day.")
        case 6 | 7:
            print("It's the weekend.")
        case _:
            print("Invalid day.")